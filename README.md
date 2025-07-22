# ncr-pakify

Converts level data from Ogmo Editor into a level pack format for Ninja Cat Remewstered. Includes an Ogmo project with entities and tilesets already set up.
- Specifically Ogmo Editor 3 from [here](https://ogmo-editor-3.github.io/). idk how compatible CE or any other fork are.

By default loads files in pack subfolders `basepak`, `sequel`, `finale` and `bouldo`.

Formats:
* `pakify.py /path/to/ninjacat/Content/levels` - build all packs.
* `pakify.py /path/to/ninjacat/Content/levels sequel finale` - build only packs `sequel` and `finale`.

Needed software:
- Python3 + Json5 package
- Ogmo Editor 3 (or compatible version)
- Ninja Cat Remewstered 1.2mg or higher (technically not needed, but good luck playing the levels you make without it)
  - You could use release version 1.1mg if you're only editing `basepak`. Other packs are non-functional as this version is hardcoded to load only `basepak` and does not have the menu to select packs.

Basic workflow:
- If you're making a new level pack, create a folder for your level pack and edit `pakify.py` to point to your folder rather than the originals.
- Add a `base.ncl` file, with the base details for the pack. Use the default level packs (except `basepak`) in this repository as examples.
- Using Ogmo Editor, open the `.ogmo` file.
- When creating levels, place them in the pack folder and name them by number like `1.json 2.json 3.json`.
- Find your Ninja Cat Remewstered's `Content/levels` folder. (or wherever you want the output `.ncl` files to go)
- Running `pakify.py /path/to/Content/levels <pack folder>` should produce `<pak>.ncl` files in the game's directory.
  - These are just `json` files with a funny extension... which doesn't even matter really.
- Finally, if you have made a new pack, make sure to add your pack's filename to the `packs.json` file so the game knows to load it.

The level pack's `glyph` uses the PICO-8 gfx format. They can be made inside PICO-8 and copy-pasted in. Remove the `[gfx]` and `[/gfx]` tags and it should just work.
- Keep the width and height bytes though, those are used to format the icon properly. Max size is 64x64px, typical size is 16x16px plus a 1px border. (18x18px total)

## Alternate levels

Alternate levels are named in the following format: `<level>_<condition>.json`, like `1_goldRush.json`
The important part is the `_`. That marks where the condition starts. You should only ever have ONE `_` in the filename.
- In theory `1_goldRush_blah blah blah.json` shouldn't break anything though... if you wanna give them recognisable names. MIGHT change in the future though!
  - You should put names BEFORE the `_` if you wanna do that. Ideally follow a format like `1-<name>_<condition>.json`, so `1-first-level_goldRush.json` or `3-pacifist-hallway_noHarm.json`

Alternates will be appended to the last processed level alphabetically. That is, having the following:

- `a.json`
- `b_goldRush.json`
- `c.json`

Would put `b` as an alternate of `a`, and `c` would be processed as Level 2:

- `a.json` - Level 1
- `b_goldRush.json` - Level 1 (with Gold Rush modifier)
- `c.json` - Level 2

Adding a level sorted after `a` and before `b_goldRush` would change the flow again:

- `a.json` - Level 1
- `b.json` or `ab.json` or `another.json` - Level 2
- `b_goldRush.json` - Level 2 (with Gold Rush modifier)
- `c.json` - Level 3

Only one condition can be used at a time; the first alternate with a matching condition wins.
- If you have the Gold Rush and No Harm modifiers enabled, then your alternates were converted as `0 = goldRush` and `1 = noHarm`, it would load the alternate level for Gold Rush mode as that is listed first.
  - You can guide pakify to process your alternates in a specific order by naming the file like `1-1_noHarm.json` and `1-2_goldRush.json`, as it processes them alphabetically. Do not add more `_`'s!

Valid alternates are the following:
- `noHarm` - No Harm modifier is enabled.
  - I use this to replace the boss fights with vault rooms, which are usually to try teaching niche mechanics like how hitting a Shield Ninja's shield with shuriken will not kill the player, or otherwise as small puzzle rooms.
- `goldRush` - Gold Rush modifier is enabled.
  - You can use this to add extra gold or an alternative layout to make gold the main focus of the level.
- `newGamePlus` - New Game Plus modifier is enabled.
  - Add more enemies, make tighter jumps, smaller platforms, it's up to you. Or subvert people's expectations and make it easier?
- `hasDoubleJump` - Player has unlocked Double-Jump.
- `hasSword` - Player has the Sword available.
- `hasShuriken` - Player has the Shuriken available.
- `elenn` - Playing as Elenn.

The lack of Easy Mode here is simply due to enemies having a property on them already to remove them if easy is enabled. Might add it if I feel like it later, or if people actually want proper easy alternates. BUT! This way you CAN combine Easy Mode with other alternates! How rare!

## Dependencies
- `json5` so json comments don't break it, otherwise should work fine if you make it `import json` instead as long as you remove any comments.
