# ncr-pakify

Converts level data from Ogmo Editor into a level pack format for Ninja Cat Remewstered. Includes an Ogmo project with entities and tilesets already set up.
- Specifically Ogmo Editor 3 from their website. idk how compatible CE or any other fork are.

By default loads files in pack folders `basepak`, `sequel`, `finale` and `bouldo` next to the `pakify.py` file (or the working dir, untested).

Needed software:
- Python3 + Json5 package
- Ogmo Editor 3 (or compatible version)
- Ninja Cat Remewstered 1.2mg or higher (technically not needed, but good luck playing the levels you make without it)
  - You could use release version 1.1mg if you're only editing `basepak`. Other packs there are non-functional as this version is hardcoded to load `basepak`.

Basic workflow:
- Edit the path near the top of the `pakify.py` script to point to your Ninja Cat Remewstered's `Content/levels` folder. (or wherever you want the output `.ncl` files to go)
- If you're making a new level pack, create a folder for your level pack and edit `pakify.py` to point to your folder rather than the originals.
- Add a `base.ncl` file, with the base details for the pack. Use the default level packs (except `basepak`) in this repository as examples.
- Using Ogmo Editor, open the `.ogmo` file.
- When creating levels, place them in the pack folder and name them by number like `1.json 2.json 3.json`.
- Running `pakify.py` should produce `<pak>.ncl` files in the game's directory.
  - These are just `json` files with a funny extension... which doesn't even matter really.
- Finally, if you are making a new pack, make sure to add your pack's filename to the `packs.json` file so the game knows to load it.

The level pack's `glyph` uses the PICO-8 gfx format. They can be made inside PICO-8 and copy-pasted in. Remove the `[gfx]` and `[/gfx]` tags and it should just work.
- Keep the width and height bytes though, those are used to format the icon properly. Max size is 64x64px, typical size is 16x16px plus a 1px border. (18x18px total)

## Dependencies
- `json5` so json comments don't break it, otherwise should work fine if you make it `import json` instead.
