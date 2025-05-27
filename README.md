# ncr-pakify

Converts level data from Ogmo Editor into a level pack format for Ninja Cat Remewstered. Includes an Ogmo project with entities and tilesets already set up.

By default loads files starting with `3`, `4`, `5`, or `6`. Each outputs to a json file with the same number. Maybe will be dynamic in future.

Format files like: `3-1.json 3-2.json 3-3.json` and it will output a `pack-3.json` file with those levels converted. You will need to insert this into a new or pre-existing level pack `.ncl` file (which are just `json` files with a funny extension... which doesn't even matter really)

Adding a level pack, copy one of the original ones, delete the `"levels"` part and replace it with the output file content, then update the other details.

Level pack glyphs for the menu can be made inside PICO-8 and copy-pasted in. Remove the `[gfx]` and `[/gfx]` tags and it should just work.
- Keep the width and height bytes though, we do use those to format the icon properly. Max size is 64x64px, typical size is 16x16px plus a 1px border. (18x18px total)
