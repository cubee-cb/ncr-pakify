# Setup

You will need:
- Ogmo Editor 3 (from [here](https://ogmo-editor-3.github.io/) or a compatible version)
- Ninja Cat Remewstered 1.2mg or higher

## Required Information

The Development Folder is in the following locations:
- Windows: `C:\Users\<user>\AppData\Roaming\cubee\ninjacat\pakify`
- Linux: `/home/<user>/.config/cubee/ninjacat/pakify`

The Custom Levels Folder is in the following locations:
- Windows: `C:\Users\<user>\AppData\Roaming\cubee\ninjacat\customPacks`
- Linux: `/home/<user>/.config/cubee/ninjacat/customPacks`

The Development Folder should be formatted like so:
- `pakify/` < Development Folder
  - `assets/` < Ogmo Project assets folder
  - `setA/` < Level Set
    - `regionA/` < Region Source
      - `levelA.json` < Ogmo Levels
      - `levelB.json`
      - `order.json` < Level Order
    - `regionB/` < Region Source
      - `levelA.json` < Ogmo Level
      - `order.json` < Level Order
    - `set.json` < Set Metadata
  - `ncr.ogmo` < Ogmo Project

That is, each "Set" of Region Packs is stored in its own folder. This is for organisational purposes, and so that it is possible to upload sequential Region Packs to the Steam Workshop.
- For example, a Level Set might contain a sequence of Region Packs that unlock one after the other.

In fact, the folder name of the Level Set is more or less irrelevent; Workshop Sets are downloaded to Steam's `workshop` folder and named with their Workshop ID.
- The Development Folder is intended only for developing Packs. To use packs from outside the workshop, add them to the Custom Levels Folder instead.

Sets will be built into a structure like so, into the Custom Levels Folder:
- `customPacks/` < Custom Levels Folder
  - `setA/` < Level Set
    - `set.json` < Set Metadata
    - `regionA.ncl` < Region
    - `regionB.ncl` < Region
  - `setB/` < Level Set
    - `set.json` < Set Metadata
    - `levels.ncl` < Region

## Basic Workflow
Usage of Ogmo Editor itself will not be covered here.
- Place the `.ogmo` file and assets folder into your Development Folder, like so: `ninjacat/pakify/ninja-cat-remewstered.ogmo` and `ninjacat/pakify/assets/`

There is a `template` Region Pack included, [here](../template).
- You can try building this (or any of the Vanilla Packs) before making your own levels if you like.

If you're making a new Region Pack:
- Go to the Level Development Folder.
- Create the Structure for your level set.
  - See [Base NCL Properties](Base%20NCL%20Properties.md) for a template.

To create a Level for a Region:
- Using Ogmo Editor, open the `.ogmo` project file.
- Find the Region's folder, then right click it and press **Create Level Here**.
- Name it whatever you like, given the following:
  - [Alternate Levels](Alternate%20Levels.md) have specific requirements for file names: do not use `_` for general names, as it will turn these levels into Alternates.

And finally, to pakify:
- Open Ninja Cat Remewstered.
- Go to the `System Menu` > `Options` > `Technical` > `Pakify`
- Select the Level Set to run through pakify, then select `Build`.
  - Level Sets will be reloaded automatically when it finishes.
- Once complete, go to `New Game` menu and see if your pack is there.

todo: Publishing to Steam Workshop:
- You may only upload Level Sets you have the source for. That is, Sets that Pakify can see.
- Go to the `System Menu` > `Options` > `Technical` > `Pakify`
- Select the Level Set to publish, then select `Publish Level Set`.
  - If the Level Set has already been published, it will be updated instead.
- Pakify will build the Level Set and upload it with the details specified in `set.json`.
  - The Set will have a `workshop.json` file added to its project folder. Do not remove or modify this; it contains the Workshop ID of the Set.

### Troubleshooting
If your pack does not appear in the `New Game` menu:
- Try running Ninja Cat Remewstered through a console, then rebuild.
  - It will provide detailed output about what exactly pakify or the Level Set importer is failing on.
- Make sure your files are formatted correctly.

Pakify doesn't see the pack:
- Make sure it's in the right folder and contains a properly-formatted `set.json`.

### `set.json` example
```json
{
  "id": "template",
  "author": "author",
  "revision": 1,
  "requireGameVersion": 1,

  "regions": [
    "templateRegion",
    "templateRegion2"
  ]
}
```

### `order.json` example
```json
[
  "1.json",
  "2.json",
  "2_goldRush.json",
  "3.json"
]

```
