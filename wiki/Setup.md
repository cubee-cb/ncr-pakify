# Setup

You will need:
- Python 3 or newer
- Ogmo Editor 3 (from [here](https://ogmo-editor-3.github.io/) or a compatible version)
- Ninja Cat Remewstered 1.2mg or higher (not *technically* required, but good luck playing the levels you make without it!)

## Required Information

The Custom Levels folder is in the following locations:
- Windows: `C:\Users\<user>\AppData\Roaming\cubee\ninjacat\customPacks`
- Linux: `/home/<user>/.config/cubee/ninjacat/customPacks`

Packs are formatted like so:
- `customPacks/`
  - `set_a/`
    - `packOrder.json`
    - `level.ncl`
  - `set_B/`
    - `packOrder.json`
    - `level.ncl`
That is, each "Set" of Packs is stored in its own folder. This is for organisational purposes, and so that it is possible to upload Sets of Level Packs to the Steam Workshop.
- For example, a Set might contain a sequence of Packs that unlock one after the other.

In fact, the folder name of the Set is irrelevent. Sets from the Workshop are named using their Workshop ID.
- Workshop Sets are downloaded to Steam's `workshop` folder; the `customPacks` folder is for creating Packs and using Packs obtained outside the Steam Workshop.

## Command Usage
* `pakify.py /path/to/ninjacat/customPacks` - build all default packs.
* `pakify.py /path/to/ninjacat/customPacks office prismHighway` - build packs `office` and `prismHighway`.

The default packs are `basepak`, `outset`, `sequel`, `finale` and `bouldo`.

### Linux Users:
The Ogmo project is pre-configured to run a bash script that builds the default packs when pressing the Star button down in the bottom-left.
It will build by default directly to the Custom Levels folder.

## Basic Workflow
You should Clone or Download this repository to begin with. Usage of Ogmo Editor itself will not be covered here.

If you're making a new Region Pack:
- Create a folder for your Region Pack next to `pakify.py`.
  - Name it something simple that you will remember.
- Create a `base.ncl` file inside this folder, with the base details for your Region Pack.
  - See [Base NCL Properties](Base%20NCL%20Properties.md) for a template.

To create a Level for your Region Pack:
- Using Ogmo Editor, open the `.ogmo` project file.
- Find your Region Pack's folder, then right click it and press **Create Level Here**.
- Name your levels in a way that, when sorted alphabetically, they are in your intended order (0-9 then a-z).
  - If your pack contains multiple world themes, it may be beneficial to adopt a `world-level` naming scheme, i.e. `1-1.json`, `1-9.json`, `2-1.json`, just to makes things clearer; the naming scheme I use personally is the following: `<world number>-<level number><alt order>_<alternate>.json`; that is:
    - `1-2.json` for the base level.
    - `1-2a_pacifism` - for a Pacifism alternate. Note the `a` used here is to make it the *first* alternate; thus taking priority.
    - `1-2b_goldRush` - for a Gold Rush alternate that will be used as long as Pacifism isn't enabled.
  - See [Alternate Levels](Alternate%20Levels.md) for more information on Alternates and Sorting Order.

And finally, pakify:
- Go to the Custom Levels folder. (see Required Information)
  - Create a folder for your Set. Its name can be whatever you like.
  - Create a `packOrder.json` file inside this folder. See below for an example.
    - Whenever you make a new Region Pack, add its filename to this file. (without the extension)
- Running `pakify.py /path/to/customLevels/<yourSetName> <yourPackName>` should produce a `<pak>.ncl` file in your Set folder.
- Opening the game now should result in your Region Pack appearing in the New Game menu.
  - If not, you can see if it was loaded at all by running the game through a console. (Konsole, Terminal, CMD, PowerShell, etc)

### `packorder.json` example
```json
[
  "outset",
  "sequel",
  "basepak",
]
```
## Developer Tools
To access the in-game Dev Menu, open the System Menu and go to `Options` > `Technical` > `Dev Menu`.

Here you can do various things, like hot-reload the level packs, grant yourself all upgrades, restore or set health, and so on. Most of these will only have a visible effect while in a level.

Entering Score Submission after using this menu will place a marker on your score, so that you can tell which scores are legitimate.

If you have access to a Debug build, the following are available:
- The Dev Menu is added to the base Pause menu while in-game.
- `Tab` will reload level packs in-place.
- `[` and `]` skip between levels.
- `T` forces the touch layers to be shown.
- `Right Alt` will stop the UI layer from rendering while held.
