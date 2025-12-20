#!/usr/bin/env python3

import os
#import json5 as json
import json
import math
from sys import platform
from sys import argv


# === defaults === #

# folder/ncl names of the packs to process. it will be `./<pack>/1.json` for Ogmo input levels and `<outputPath>/<pack>.ncl` for output level data
pakFiles = ["basepak", "outset", "sequel", "finale", "bouldo"]

outputPath = None


# === other code below === #

print("pakify for ninja cat remewstered!")

if len(argv) > 1:
  outputPath = argv[1]

  if len(argv) > 2:
    pakFiles = argv[2::]

if outputPath is None:
  print("please specify the output directory")
  exit()

if not os.path.exists(outputPath):
  print("output directory does not exist: " + outputPath)
  exit()

outPaks = list(filter(lambda x: x.endswith(".ncl") and any(pak in x for pak in pakFiles), os.listdir(outputPath)))
print("writing to:", outputPath)
print("building paks:", pakFiles)
if len(outPaks) > 0:
  print("the following paks already in the output directory will be overwritten:", outPaks)
  input("is this ok? (press enter to continue, or ctrl+c to cancel)")

for pak in pakFiles:
  print("processing pak \"" + pak + "\"")
  levels = []

  files = os.listdir(os.path.join(".", pak))
  files.sort()
  print("reading: " + str(files))


  jsonFiles = list(filter(lambda x: x.endswith('.json'), files))
  jsonFiles.sort()

  # todo: process levels by incrementing index so altlevels don't get added separately
  altLevelsCount = 0
  for jsonFile in jsonFiles:
    baseName = os.path.splitext(jsonFile)[0]

    level = {
      "theme": "world1",
      "music": "sneaking",
      "spawn": {"x": 0, "y": 0},
      "entrance": "rappel",
      "objects": [],
      "tilemap": []
    }

    parent = None
    altLevel = False
    altLevelKey = ""

    # this is an alt level
    if "_" in jsonFile:
      parent = levels[-1]
      altLevel = True
      altLevelKey = baseName.split('_')[1]
      print("treating", jsonFile, "as an alternate for the previous level")

    # this is NOT an alt level
    else:
      print("converting level", jsonFile)
      level["alternateMaps"] = {}

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
    level["theme"] = layers.get("tiles").get("tileset") or "world1"

    # port layers.tiles.data2D to ncl format
    for row in layers.get("tiles").get("data2D"):
      level["tilemap"].append(list(map(lambda x: -1 if x < 0 else x, row)))

    # port layers.entities.entities to ncl entities
    for ogmoEntity in layers.get("entities").get("entities"):

      values = ogmoEntity.get("values")

      # if this is the start point, set start point instead
      if ogmoEntity.get("name") == "start point":
        level["spawn"]["x"] = math.floor(ogmoEntity.get("x") / 8)
        level["spawn"]["y"] = math.floor(ogmoEntity.get("y") / 8)
        level["entrance"] = "rappel"

        if values:
          level["entrance"] = values.get("entrance") or "rappel"
        continue

      # convert ogmo entity format to ncl
      entity = {
        "id": "ninja",
        "x": 0,
        "y": 0,
        "flipped": False
      }
      entity["id"] = ogmoEntity.get("name") or "ninja"
      entity["x"] = math.floor(ogmoEntity.get("x") / 8) or 0
      entity["y"] = math.floor(ogmoEntity.get("y") / 8) or 0
      entity["flipped"] = ogmoEntity.get("flippedX") or False

      # optional
      if values:
        if values.get("easy"):
          entity["easy"] = True

      level["objects"].append(entity)

    if altLevel:
      parent["alternateMaps"][altLevelKey] = level
      altLevelsCount += 1
    else:
      levels.append(level)

  # generate levels file
  print("converted", len(levels), "levels,", altLevelsCount, "alt levels")

  # write file
  
  baseNclPath = os.path.join(pak, "base.ncl") # path for the base ncl data for the level pack
  outputNclPath = os.path.join(outputPath, pak + ".ncl") # path to write final ncl to
  
  content = ""
  with open(baseNclPath, 'r') as file:
    fileContent = file.read()

    # strip comments
    for line in fileContent.split("\n"):
      content += line.split("//")[0] + "\n"
  
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
