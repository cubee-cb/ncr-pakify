# ncr-pakify

Converts level data from Ogmo Editor into a level pack format for Ninja Cat Remewstered. Includes an Ogmo project with entities and tilesets already set up.

By default loads files in pack folders `sequel`, `finale` and `bouldo` next to the `pakify.py` file (or the working dir, untested).

Format files like: `1.json 2.json 3.json` inside pack's folder and it will output a `<pack>.ncl` file to the output dir. These are just `json` files with a funny extension... which doesn't even matter really.

Adding a level pack, copy one of the original ones, delete the `"levels"` part and replace it with the output file content, then update the other details. Finally, if you are making a new pack, add the pack's filename to the `packs.json` file so the game knows to load it.

Level pack glyphs for the menu use the PICO-8 gfx format. They can be made inside PICO-8 and copy-pasted in. Remove the `[gfx]` and `[/gfx]` tags and it should just work.
- Keep the width and height bytes though, those are used to format the icon properly. Max size is 64x64px, typical size is 16x16px plus a 1px border. (18x18px total)

Depends on `json5` so json comments don't break it, otherwise should work fine with normal `json`.
