# ncr-pakify

Converts level data from Ogmo Editor into the region pack format for Ninja Cat Remewstered.

Included is an Ogmo project with all of the entities and tilesets already set up.

## Usage

### Formats:
* `pakify.py /path/to/ninjacat/Content/levels` - build all default packs.
* `pakify.py /path/to/ninjacat/Content/levels office prismHighway` - build packs `office` and `prismHighway`.

The default packs are `basepak`, `outset`, `sequel`, `finale` and `bouldo`.

### Required software:
- Python3
- Ogmo Editor 3 (from [here](https://ogmo-editor-3.github.io/) or a compatible version)
- Ninja Cat Remewstered 1.2mg or higher (not *technically* required, but good luck playing the levels you make without it)
  - While it may be possible to use release version 1.1mg, it is more difficult due to various small changes in level format, and the menu is hardcoded to only play `basepak`. Assets, entities, mechanics and changes from newer worlds are also not present and will use fallbacks, be ignored or crash.

### Basic workflow:
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

## Specifics

### Pack Glyph

The `base.ncl` `glyph` property uses the PICO-8 gfx format. They can be made inside PICO-8 and copy-pasted in (the Edu version should work fine for this use case). It will be shown in the New Game screen alongside the other packs.
- Omitting/removing the pack glyph will result in a generic icon being used. If you want your pack to be easily recognisable, make sure to give it a cool icon!

Remember to remove the `[gfx]` and `[/gfx]` tags, but keep the width and height bytes. These are used to decode the glyph properly. Typical glyph size is 16x16px plus a 1px border. (32x32px sprite)

`[gfx]WWHHxxxxxxxxxxxxxxxx[/gfx]` -> `WWHHxxxxxxxxxxxxxxxx`

Pack Glyphs can be up to 128x128px in size (the same size as the PICO-8 spritesheet)

### Alternate Levels

Alternate levels are named in the following format: `<level>_<condition>.json`, like `1_goldRush.json`
The important part is the `_`. That marks where the condition starts. You should only ever have ONE `_` in the filename.
- In theory `1_goldRush_blah blah blah.json` shouldn't break anything though... if you wanna give them recognisable names. MIGHT change in the future though!
  - I would recommend putting names BEFORE the `_` if you wanna do that. Ideally follow a format like `<index>-<name>_<condition>.json`, so `1-first-level_goldRush.json` or `3-pacifist-hallway_pacifism.json`

Alternates will be appended to the last processed level alphabetically. That is, having the following:

- `1.json`
- `2_goldRush.json`
- `3.json`

Would put `2_goldRush` as an alternate of `1`, and `3` would be processed as Level 2:

- `1.json` - Level 1
- `2_goldRush.json` - Level 1 (Gold Rush alternate)
- `3.json` - Level 2

Adding a level sorted after `1` and before `2_goldRush` would change the flow again:

- `1.json` - Level 1
- `2.json` or `22.json` or `1a.json` - Level 2
- `2_goldRush.json` - Level 2 (Gold Rush alternate)
- `3.json` - Level 3

Only one condition can be used at a time; the first alternate with a matching condition wins.
- If you have the Gold Rush and Pacifism modifiers enabled, and your alternates were converted as `0 = goldRush` and `1 = pacifism` (as they would be by alphabetical order), the game would load the alternate level for Gold Rush mode as that is listed first.
  - You can guide pakify to process your alternates in a specific order by naming the file like `3a_pacifism.json` and `3b_goldRush.json`, as it processes them alphabetically. Do not add more `_`'s!
  - This is helpful if for example your `goldRush` alternate is impossible to complete when Pacifism mode is enabled.

Valid alternates are the following:
- `pacifism` - Pacifism modifier is enabled.
  - I use this to replace the boss fights with vault rooms, which usually try teaching niche mechanics like how hitting a Shield Ninja's shield with shuriken will not kill the player, or otherwise as small puzzle rooms.
- `perfection` - Perfection modifier is enabled.
  - Maybe your level is really precise. You can make an alternate to make it easier to not make a mistake.
- `guardBell` - Guard Bell modifier is enabled.
  - Maybe you want to prevent people from cheesing your level. You could make an alternate tailored for Guard Bell's hitpoint system? Or troll them, idk it's up to you.
- `goldRush` - Gold Rush modifier is enabled.
  - You could use this to add extra gold or an alternative layout to make gold the main focus of the level.
- `newGamePlus` - New Game Plus modifier is enabled.
  - Add more enemies, make tighter jumps, smaller platforms, it's up to you. Or subvert people's expectations and make it easier?
- `elenn` and `notElenn` - Playing as Elenn or not.
  - This can be used to make challenges tailored for Elenn's faster, more slippery movement.
- `hasDoubleJump` and `notDoubleJump` - Player has unlocked Double-Jump.
  - If your pack has any extra exits where the player may not obtain Double Jump, you can check for that here.
- `hasBow` and `notBow` - Player has or doesn't have the Bow weapon.
  - If your pack has any extra exits where the player may not obtain the Bow, you can check for that here.
- `hasSword` and `notSword` - Player has or doesn't have the Sword weapon.
  - If your pack has any levels where the player may not have the Sword, but needs it, you can check for that here.
- `hasShuriken` and `notShuriken` - Player has or doesn't have the Shuriken weapon.
  - If your pack has any levels where the player may not have Shuriken, but needs them, you can check for that here.

## Notes
- `.ncl` is short for Ninja Cat Level. A holdover from early development where each level was an individual file instead of being grouped in packs. They are just `json` files internally, but the extension makes it more obvious what the file is for.
- `basepak`'s `base.ncl` is pre-generated NCL with all the levels included, as it was generated inside PICO-8 directly from the original game's map data rather than an Ogmo project. This is why there are seemingly no levels inside the pack folder.
