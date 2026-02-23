# Setup (Integrated)

This page is for the version of pakify built-in to Ninja Cat Remewstered. For the Python version, see [Setup (pakify Standalone)](Setup%20Standalone.md).

You will need:
- Ogmo Editor 3 (from [here](https://ogmo-editor-3.github.io/) or a compatible version)
- Ninja Cat Remewstered 1.2mg or higher

## Required Information

The Pakify Folder is in the following locations:
- Windows: `C:\Users\<user>\AppData\Roaming\cubee\ninjacat\pakify`
- Linux: `/home/<user>/.config/cubee/ninjacat/pakify`
- Linux (Steam Flatpak): `/home/<user>/.var/app/com.ValveSoftware.Steam/.config/cubee/ninjacat/pakify`

The Pakify Folder is only for developing Level Sets. To play Level Sets from outside the Workshop, add them to the Custom Levels Folder instead:
- Windows: `C:\Users\<user>\AppData\Roaming\cubee\ninjacat\customLevels`
- Linux: `/home/<user>/.config/cubee/ninjacat/customLevels`
- Linux (Steam Flatpak): `/home/<user>/.var/app/com.ValveSoftware.Steam/.config/cubee/ninjacat/customLevels`

The Pakify Folder should be formatted like so:
- `pakify/` < Pakify Folder
  - `.assets/` < Ogmo Project assets folder
  - `setA/` < Level Set
    - `regionA/` < Region Folder
      - `levelA.json` < Ogmo Levels
      - `levelB.json`
      - `order.json` < Level Order
      - `region.json` < [Region Properties](Region%20Properties.md)
    - `regionB/` < Region Folder
      - `levelA.json` < Ogmo Level
      - `order.json` < Level Order
      - `region.json` < [Region Properties](Region%20Properties.md)
    - `set.json` < [Set Properties](Set%20Properties.md)
  - `ninja-cat-remewstered.ogmo` < [Ogmo Project](Ogmo%20Project.md)

That is, each "Set" of Region Packs is stored in its own folder. This is for organisational purposes, and so that it is possible to group Campaigns of sequential Regions as one distinct item.

Here's a visual for a Level Set folder:

![a file browser inside a level set's folder](images/pakfolderset.png)

And another for a Region folder:

![a file browser inside a region's folder](images/pakfolderregion.png)

Linux people: the above images were taken inside a Wine Prefix so Windows people can follow the exact path in the top bar; please use the Linux path unless you happen to be running the Windows version under Wine/Proton, though note issues with this setup may not be supported; the Native Linux version is the first-class build here.

Pakify will Build sets directly into the Custom Levels Folder - if we build `setA`, then we will get the following structure:
- `customPacks/` < Custom Levels Folder
  - `setA/` < Level Set
    - `set.json` < Set Metadata
    - `regionA.ncl` < Region
    - `regionB.ncl` < Region

## Basic Workflow
Usage of Ogmo Editor itself will not be covered here.

### Prerequisites
Place the `.ogmo` file and `.assets` folder from this repository into your Pakify Folder, like so:
- `pakify/`
  - `.assets/`
  - `ninja-cat-remewstered.ogmo`

These files are required for level creation and are not included with the game. To obtain them:
- Go to the main [GitHub Page](https://github.com/cubee-cb/ncr-pakify/).
- Click the green `Code` button and then `Download ZIP`.
- Place the ZIP file into the Pakify Folder, then extract it.
  - If the ZIP gets extracted into its own sub-folder, move its content back into the Pakify Folder.

### Steps
There is an example Level Set included, [`exampleSet`](../exampleSet).
- You can copy this folder directly into your Pakify Folder if you like.

#### If you're making a new Level Set or Region:
- Go to the Level Pakify Folder.
- Create the Structure for your level set.
  - See [Set Properties](Set%20Properties.md) and [Region Properties](Region%20Properties.md) for templates, and [Required Information](#required-information) for file structure.

![a file browser inside a level set's folder](images/pakfolderset.png)

![a file browser inside a region's folder](images/pakfolderregion.png)

#### To create a Level for a Region:
- Using Ogmo Editor, open the `.ogmo` project file.
- Find the Region's folder, then right click it and press **Create Level Here**. Name it whatever you like.
  - Remember to add it into the Region's `order.json`. See [Alternate Levels](Alternate%20Levels.md) for modifier-specific level replacement.

![image showing the previous steps in ogmo editor](images/ogmonew.png)

#### And finally, to pakify:
- Open Ninja Cat Remewstered.
- Go to the Title Screen, open the System Menu, and select `Pakify`.
  - Or from `Options` anywhere: `Options` > `Technical` > `Pakify`

![pakify root menu](images/pakroot.png)

- Select the Level Set to run through pakify, then select `Build`.
  - !! You will be returned to the title screen automatically when it finishes.

![pakify set menu](images/paksets.png)

![pakify build button](images/pakbuild.png)

![pakify success banner](images/pakok.png)

- Once complete, go to `New Game` in the main menu and see if your Regions are there.

![new game screen](images/paknewgame.png)

#### Publishing to Steam Workshop:
Sets can only be published to the Steam Workshop using the Steam build of the game, while Steam is running.
- To check if this is the case, either see if the Sets listed by Pakify have a Publish option, or check if the console output has `connected to steam!` followed by a greeting (e.g. `hello cubee!`).

You may only upload Level Sets you have the source for. That is, Sets that Pakify can see. Make sure you have `title` and `description` set up for your Level Set.
- Go to the Title Screen, open the System Menu, and select `Pakify`.
  - Or from `Options` anywhere: `Options` > `Technical` > `Pakify`

![pakify root menu](images/pakroot.png)

- Select the Level Set you want to publish, then select `Publish/Update set`.
  - If the Level Set has already been published, it will be updated instead.
    - If the item was deleted from Steam Workshop, the game will attempt to create a new item instead.
  - !! You will be returned to the title screen automatically when it finishes.

![pakify set menu](images/paksets.png)

![pakify publish button](images/pakpublish.png)

- Pakify will build the Level Set and upload it to the Workshop using the details specified in `set.json`. This may take a few moments.
  - The Set will have a `workshop.json` file added to its project folder. Do not remove or modify this unless you want to upload the Level Set again as a new item.
  - This will not build the pack to the Custom Levels folder; you will need to Pakify Build separately to update your local copy.
  - If the upload fails, please check Troubleshooting below.

### Troubleshooting
**If your pack does not appear in the `New Game` menu:**
- Try running Ninja Cat Remewstered through a console, then rebuild.
  - It will provide detailed output about what exactly Pakify or the Level Set importer is failing on -> look for lines tagged with `[pakify]` or `[pakify (ERROR)]`.
- Make sure your files are formatted correctly.

**Pakify doesn't see the pack:**
- Make sure it's in the right folder and contains a properly-formatted `set.json`.

**Publish fails:**
- Try running Ninja Cat Remewstered through a console, then publish again.
  - It will provide detailed output about what exactly Pakify is failing on -> look for lines tagged with `[pakify]` or `[pakify (ERROR)]`.
- Make sure your files are formatted correctly.
- Check that you have agreed to the Steam Subscriber Agreement / Workshop ToS.

### `order.json` example
Format:
- `<filename>` - e.g. `epicLevel1.json`
- `<filename>:<alternate>` - e.g. `epicLevel1.json:pacifism`

The indentation here is optional; I use it to more easily tell which levels are Alternates.
```json
[
  "1.json",
  "2.json",
    "2-goldrush.json:goldRush",
  "3.json"
]

```
