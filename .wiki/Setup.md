# Setup

You will need:
- Ogmo Editor 3 (from [here](https://ogmo-editor-3.github.io/) or a compatible version)
- The Ogmo Project and `.assets/` folder from this repository
- Ninja Cat Remewstered V1.2mg or higher

## File Locations

The Pakify Folder is in the following locations:
- Windows: `C:\Users\<user>\AppData\Roaming\cubee\ninjacat\pakify`
- Linux: `/home/<user>/.config/cubee/ninjacat/pakify`
- Linux (Steam Flatpak): `/home/<user>/.var/app/com.ValveSoftware.Steam/.config/cubee/ninjacat/pakify`

The Pakify Folder is only for developing Level Sets. To play Level Sets from outside the Workshop, add them to the Custom Levels Folder instead:
- Windows: `C:\Users\<user>\AppData\Roaming\cubee\ninjacat\customLevels`
- Linux: `/home/<user>/.config/cubee/ninjacat/customLevels`
- Linux (Steam Flatpak): `/home/<user>/.var/app/com.ValveSoftware.Steam/.config/cubee/ninjacat/customLevels`

The `<user>` folder here is a placeholder. Usually, this would be your user's home folder, commonly referred to with either your Username or "Home". i.e. if my username is `cubee`:
- Windows: I open File Explorer and go to "cubee" in the sidebar, or `C:\Users\cubee\`.
- Linux KDE / Steam Deck (Desktop Mode): I open Dolphin and go to "Home" in the sidebar, or `/home/cubee/`.

## Pakify Folder Structure

The Pakify Folder should be formatted like so (items with a trailing `/` are folders):
- `pakify/` < Pakify Folder
  - `.assets/` < Ogmo Project assets folder
  - `setA/` < Level Set Folder
  - `setB/` < Level Set Folder
  - `setC/` < Level Set Folder
  - `ninja-cat-remewstered.ogmo` < [Ogmo Project](Ogmo%20Project.md)

Level Sets use the following structure. Using `setA` as an example:
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
  - `preview.png`
  - `set.json` < [Set Properties](Set%20Properties.md)

That is, each Level Set is stored in its own folder. This is for organisational purposes, and so that it is possible to group sequential Regions as one distinct item.

Here's a visual for a Level Set folder:

![a file browser inside a level set's folder](images/pakfolderset.png)

And another for a Region folder:

![a file browser inside a region's folder](images/pakfolderregion.png)

Linux/SteamOS people: the above images were taken inside a Wine Prefix so Windows people can follow the exact path in the top bar; please use the Linux path unless you happen to be running the Windows version under Wine/Proton.

## Output

Pakify will Build sets directly into the Custom Levels Folder. See [Basic Workflow](Basic%20Workflow.md) for how to use Pakify to Build a Level Set.

If we build `setA`, then we will get the following structure:
- `customPacks/` < Custom Levels Folder
  - `setA/` < Level Set
    - `set.json` < Set Metadata
    - `regionA.ncl` < Region
    - `regionB.ncl` < Region

If you wish to Publish your set to the Steam Workshop, see [Steam Workshop](Steam%20Workshop.md). A Publish will not build to the Custom Levels folder, so make sure to Build and test your Region before publishing!

## Templates

### `order.json`
Formats:
- `<filename>` - e.g. `epicLevel1.json` for a single base level.
- `<filename>:<alternate>` - e.g. `epicLevel1.json:pacifism` for an [Alternate Level](Alternate%20Levels.md).

Here's a template. I use indentation to more easily tell which levels are Alternates:
```json
[
  "1.json",
  "2.json",
    "2-goldrush.json:goldRush",
  "3.json"
]

```

### `region.json`

See [Region Properties](Region%20Properties.md).

### `set.json`

See [Set Properties](Set%20Properties.md).
