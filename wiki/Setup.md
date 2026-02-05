# Setup

## Required software
- Python3
- Ogmo Editor 3 (from [here](https://ogmo-editor-3.github.io/) or a compatible version)
- Ninja Cat Remewstered 1.2mg or higher (not *technically* required, but good luck playing the levels you make without it!)
  - While it may be possible to use release version 1.1mg, it is more difficult due to various small changes in level format, and the menu is hardcoded to only play `basepak`. Assets, entities, mechanics and changes from newer worlds are also not present and will use fallbacks, be ignored or crash.

## Command formats
* `pakify.py /path/to/ninjacat/Content/levels` - build all default packs.
* `pakify.py /path/to/ninjacat/Content/levels office prismHighway` - build packs `office` and `prismHighway`.

The default packs are `basepak`, `outset`, `sequel`, `finale` and `bouldo`.

## Basic workflow
- If you're making a new region pack, create a folder for your region pack next to `pakify.py`.
- Add a `base.ncl` file inside the new folder, with the base details for the pack. Use the default region packs (except `basepak`) in this repository as examples.
- Using Ogmo Editor, open the `.ogmo` project file.
- When creating levels, place them in the pack folder and name them by number like `1.json`, `2.json`, `3.json`.
  - If your pack contains multiple "worlds", it may be beneficial to adopt a `world-level` naming scheme, i.e. `1-1.json`, `1-9.json`, `2-1.json`, just to makes things clearer.
  - The naming scheme I use personally is the following: `<world number>-<level number><alt order>_<alternate>.json`; that is:
    - `1-2.json` for the base level.
    - `1-2a_pacifism` - for a Pacifism alternate. Note the `a` used here is to make it the *first* alternate; thus taking priority.
    - `1-2b_goldRush` - for a Gold Rush alternate that will be used as long as Pacifism isn't enabled.
- Find the `Content/levels` folder in your Ninja Cat Remewstered install. (or wherever you want the output `.ncl` files to go)
- Running `pakify.py /path/to/Content/levels` should produce `<pak>.ncl` files in the game's directory.
  - You can also specify which packs to build after the path. e.g. `pakify.py /path/to/Content/levels outset sequel` would build only the packs `outset` and `sequel`.
- Finally, if you have made a new pack, add your pack's filename to the `packs.json` file so the game knows to load it.
