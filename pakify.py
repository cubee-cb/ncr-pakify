#!/usr/bin/env python3

import os
import json5 as json
import math

# i'm lazy. this should be platform-agnostic
outputPath = "C:\\Users\\jaymo\\source\\repos\\ninjacat-remewstered\\Ninja Cat Desktop 383\\Content\\levels"

# folder/ncl names of the packs. it will be `./<pack>/1.json` for Ogmo input levels and `<outputPath>/<pack>.ncl` for output level data
pakFiles = ["basepak", "sequel", "finale", "bouldo"]


print("pakify 0.1 for ninja cat remewstered!")

outPaks = list(filter(lambda x: x.endswith(".ncl") and any(pak in x for pak in pakFiles), os.listdir(outputPath)))
print("working on paks:", pakFiles)
print("found corresponding output paks:", outPaks)

for pak in pakFiles:
  print("processing pak", pak)
  levels = []

  files = os.listdir(os.path.join(".", pak))
  files.sort()
  print("reading: " + str(files))


  jsonFiles = list(filter(lambda x: x.endswith('.json'), files))
  jsonFiles.sort()

  # todo: process levels by incrementing index so altlevels don't get added separately
  for jsonFile in jsonFiles:
    
    # todo: check for altlevels and append them to the current level under "alternateMaps"
    # currently, just skip any sublevels that happen to be in here
    altLevel = False
    if "_" in jsonFile:
      print(jsonFile, "is an alternate level!")
      altLevel = True
      continue
    #altLevels = list(filter(lambda x: x.startswith() and '_' in x, files))


    print("converting", jsonFile)
    
    level = {
      "theme": "world1",
      "music": "sneaking",
      "spawn": {"x": 0, "y": 0},
      "objects": [],
      "tilemap": []
    }

    data = ""
    with open(os.path.join(".", pak, jsonFile), 'r') as file:
      data = file.read()

    if data == "":
      continue

    # decode json
    ogmo = json.loads(data)
    layers = dict()
    for layer in ogmo.get("layers"):
      if layer["name"] == "tiles":
        layers["tiles"] = layer
      elif layer["name"] == "entities":
        layers["entities"] = layer

    # process data for music, etc
    values = ogmo.get("values")
    level["music"] = values.get("music")

    # port layers.tiles.tileset to ncl format

    # port layers.tiles.data2D to ncl format
    for row in layers.get("tiles").get("data2D"):
      level["tilemap"].append(list(map(lambda x: 0 if x < 0 else x, row)))

    # port layers.entities.entities to ncl entities
    for ogmoEntity in layers.get("entities").get("entities"):

      # if this is the start point, set start point instead
      if ogmoEntity.get("name") == "start point":
        level["spawn"]["x"] = math.floor(ogmoEntity.get("x") / 8)
        level["spawn"]["y"] = math.floor(ogmoEntity.get("y") / 8)
        continue

      values = ogmoEntity.get("values")

      # convert ogmo entity format to ncl
      entity = {
        "id": "ninja",
        "x": 0,
        "y": 0,
        "flipped": False
      }
      entity["id"] = ogmoEntity.get("name")
      entity["x"] = math.floor(ogmoEntity.get("x") / 8)
      entity["y"] = math.floor(ogmoEntity.get("y") / 8)
      entity["flipped"] = ogmoEntity.get("flippedX")

      # optional
      if values.get("easy"):
        entity["easy"] = True

      level["objects"].append(entity)

    levels.append(level)

  # generate levels file
  print("converted", len(levels), "levels")

  # write file
  
  baseNclPath = os.path.join(pak, "base.ncl") # path for the base ncl data for the level pack
  outputNclPath = os.path.join(outputPath, pak + ".ncl") # path to write final ncl to
  
  content = ""
  with open(baseNclPath, 'r') as file:
    content = file.read()
  
  print("processing json and writing ncl file...")
  nclLevelPak = json.loads(content)

  # only replace levels if there are any, otherwise just passthrough whatever's already in the file (used for basepak since that was a separate conversion from pico-8)
  if len(levels) > 0:
    nclLevelPak["levels"] = levels
  out = "// generated ncl from pakify by cubee\n" + json.dumps(nclLevelPak) + ""
  
  # write ncl file
  with open(outputNclPath, 'w') as file:
    file.write(out)
  #print(outputNclPath )

print("")
print("done!")
