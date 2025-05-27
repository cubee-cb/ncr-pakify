#!/usr/bin/env python3

import os
import json
import math

print("pakify 0.1 for ninja cat remewstered!")

paks = [3, 4, 5, 6]

files = os.listdir()
files.sort()

print("reading: " + str(files))

for pak in paks:
  print("processing pak", pak)
  levels = []
  jsonFiles = filter(lambda x: x.startswith(str(pak)) and x.endswith('.json'), files)

  for jsonFile in jsonFiles:
    level = {
      "theme": "world1",
      "music": "sneaking",
      "spawn": {"x": 0, "y": 0},
      "objects": [],
      "tilemap": []
    }

    data = ""
    with open(jsonFile, 'r') as file:
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
  out = "// generated ncl from pakify by cubee\n\"levels\": " + json.dumps(levels) + ""
  outFile = "pack-" + str(pak) + ".json"
  #print(out)
  with open(outFile, 'w') as file:
    file.write(out)

print("done!")
