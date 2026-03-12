# Region Properties
## Template

Some properties are omitted; see below for a full list of properties and their allowed values.

```json
{
  "id": "template",
  "unlocked": true,
  "hidden": false,

  "displayName": {
    "english": "Template Region",
    "meowlang": "meow"
  },
  "description": {
    "english": "A template ripe for editing!",
    "meowlang": "meow meow meow"
  },

  "glyph": "202000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000dddddddd0000000000000000000000ddd677776ddd0000000000000000000dd6777777776dd00000000000000000dd677777737776dd0000000000000000d67777773337776d000000000000000dd777777bb377777dd00000000000000d677777bbb7777776d00000000000000d677773bb77777776d00000000000000d6777b33777777776d00000000000000d6677bbddddd77766d00000000000000d6667777777777666d00000000000000d7666677777766667d00000000000000dd66666666666666dd000000000000000d76666666666667d0000000000000000dd766666666667dd00000000000000000dd7766666677dd0000000000000000000ddd777777ddd0000000000000000000000dddddddd00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
  "worldTheme": "world1",
  "worldSky": "night",
  "worldFade": "cut"
}
```

## Properties

### `id` - Identifier
Used internally for scoreboards, save files, and the like. This is not typically visible to the player. (see `displayName` and `description`)

When choosing an `id`, try to think of something unique to avoid conflicting with other people's regions. A good idea might be to include your username with it, or add some random words.
You do not need to worry about this too much for Workshop packs, as their Workshop ID will be added to the Region IDs automatically when uploading.
- `<region-id>.<workshop-id>`
- `demake by cubee.3671698094`
- `plateplus.3671342679`

Sets from the Workshop will use different scoreboards due to the above.
When building your Level Set, don't accommodate for the changing Region ID (for example, with rewards); as long as your Set has working IDs locally, Pakify will handle it for you.

Some examples for "unique" names, for distribution outside Steam Workshop:
- `NinjaCatPlayer UltraChallengePack`
- `doomcastle by creampuff`
- `kaizo observatory - charlise hopscotch`
- `orangejuice ledgehop inmost 20mtd`

If the game tries to load a region with an `id` that is already taken, the new region will be skipped and a warning popup will be shown.
- In `save.json`, you can set it to replace loaded regions instead and/or turn off the warning popups. (for example, if you're editing the Vanilla regions)

### `displayName` - Name of the Region
Shown in the New Game menu under the Region Glyph.
Contains a Dictionary of language keys, with corresponding text.

There is a very limited amount of space, so keep these names within 2-3 shorter words.

### `description` - Short Description.
Shown in the New Game menu at the top of the screen.
Contains a Dictionary of language keys, with corresponding text.

Descriptions can be a lot longer than the Display Name, but try to keep them within one line.

### `author` - Creator of the Region.
Currently unused. You can use this to credit whoever made this Region directly.

If multiple people worked on it, preferably use comma separation.

### `revision` - Version of the Region.
Currently unused.

### `unlocked` - Unlocked by Default
Set this to `false` if you would like this region to be locked initially.

This region can then be added as a `reward` for completing a different region, for example as part of a larger campaign.

### `hidden` - Hide when Locked
Set this to `true` if you would like this region to be hidden until it is unlocked; it will not appear in the menus, nor the leaderboards.

Unlocking a hidden region will display alternative unlock text, saying that a **secret region** was found.

### `glyph` - Region Glyph
The `glyph` property expects a string in the PICO-8 gfx string format. It will be shown in the New Game and Leaderboard menus alongside the other regions.
Glyphs can be made inside PICO-8 and copy-pasted directly from the sprite editor to the text file. (the web-based [Education Edition](https://www.pico-8-edu.com/) works fine for this use case) Remember, Black is treated as transparent and will not be shown.

Notes:
- Typical glyph size is 16x16px plus a 1px border, drawn in the centre of a 32x32px sprite, though they can be up to 128x128px in size (the same size as the PICO-8 spritesheet)
- The Title Menu will show where each Region is sourced from, using a little icon that is overlayed onto the lower-right corner their Glyphs. This may cover part of the Glyph, so try not to put anything important there.
- Omitting/removing the region glyph will result in a generic icon being used. If you want your region to be easily recognisable, make sure to give it a cool icon!
- Because these use the PICO-8 format, and to keep thing simple, the extra colours and transparency used in the rest of the game are not supported.

```
// pico-8 sprite string format
// WW HH are the sprite Width and Height, in hex (e.g. 1010 for a 16x16 sprite)
// xxxx is the piXel data, in hex
// [gfx]WWHHxxxxxxxxxxxxxxxx[/gfx]

// used as a region glyph (note the [gfx] tags are optional)
  "glyph": "[gfx]WWHHxxxxxxxxxxxxxxxx[/gfx]",
  "glyph": "WWHHxxxxxxxxxxxxxxxx",
```

### `worldTheme` - Background
World background to use on the region's leaderboard page. Valid values:
- `world1` - Sky Mountains
- `world2` - Sky Mountains with trees and houses. (Skyscrapers in Old Style)
- `world3` - Forest
- `world4` - Underground Cavern

### `worldSky` - Sky
Sky variant to use on the region's leaderboard page. Valid values:
- `night` - Blue night sky with moon.
- `underground` - Black sky with no moon or stars.
- `dawn` - An orange sky. Subject to change.
- `aurora` - Unfinished

### `worldFade` - Fade Style
Fade style to use on the region's leaderboard page. Valid values:
- `cut` - Standard triangular fade pattern.
- `circle` - Large circle fade pattern. (Small circles in Old Style)
- `square` - Large square fade pattern. (Small squares in Old Style)
- `special` - Star fade. (Weird pattern in Old Style)

### `rewards` - Region-completion Rewards
Format: `<type>:<item>` or `<condition>;<type>:<item>`

These allow you to unlock certain things for the player when they complete your region.

Valid items for type `modifier` (case and spacing insensitive):
- `elenn` - Unlock the Elenn modifier. (see `sequel`)
  - This will also grant the Steam Achievement.
- `mirror mode` - Unlock the Mirror Mode modifier. (see `basepak`)
  - This will also grant the Steam Achievement.

Some modifiers cannot be unlocked through Region rewards:
- New Game Plus unlocks when any built-in Region is completed.
- Randomiser unlocks when any built-in Region is completed in Mirror Mode.

Valid items for type `region`:
- The `id` of any Region. If the Region isn't loaded, this will be done without creating the notification, and the Region will be unlocked if it is loaded in the future.
- You do not need to change this Region ID for Workshop uploads; Pakify will automatically update them.

Valid for `condition` (case and spacing insensitive):
- `guard bell` - Unlock only if Guard Bell is active.
- `gold rush` - Unlock only if Gold Rush is active.
- `one life` - Unlock only if One Life is active.
- `perfection` - Unlock only if Perfection Mode is active.
- `pacifism` - Unlock only if Pacifism Mode is active.
- `new game plus` - Unlock only if New Game Plus is active.
- `randomiser` - Unlock only if Randomiser is active.
- `mirror` - Unlock only if Mirror Mode is active.
- `elenn` - Unlock only if playing as Elenn.

Example:
```
  "rewards": [
    "region:scary castle", // unlock region with id "scary castle"
    "modifier:elenn", // unlock Elenn
    "gold rush;region:gilded castle" // unlock region "gilded castle" if beaten with Gold Rush enabled
  ],
```

### `startingItems` and `startingItemsNewGamePlus`
Optional lists of items to grant the player when starting a new game:
- `startingItemsNewGamePlus` is used in New Game Plus and Mirror Mode; both are what I would call "continuation" modes.
- `startingItems` is used for all other modes.

These can be set to empty lists to remove all starting items, or omitted completely to use the defaults.

A good rule of thumb for `startingItemsNewGamePlus` is to just add all upgrades the player can obtain throughout this Region. This way, it's a true New Game Plus, as the player restarts with the same upgrades! Especially since this is used for Mirror Mode; this should contain at least the minimum items a player would require to complete any arbitrary stage.

When `startingItems` is not specified, the game will start Ensy with Shuriken, and Elenn with the Sword.
- You could set this to contain only `"shuriken"` or `"sword"` if you want/need both characters to start with the same item.

When `startingItemsNewGamePlus` is not specified, it will fall back to the normal `startingItems`, and if that's also not set, it will grant the following default items:
- Shuriken
- Sword
- Double Jump

Examples of all valid values (case and spacing insensitive):
```
  "startingItems": [
    "shuriken",
    "sword",
    "bow",
    "double jump",
    "climbing claws"
  ],

  "startingItemsNewGamePlus": [
    "shuriken",
    "sword",
    "bow",
    "double jump",
    "climbing claws"
  ],
```

Some work with multiple names:
- Skuriken - `shuriken`, `star`
- Jump Scroll - `double jump`, `jump scroll`, `scroll`
- Climbing Claws - `climbing claws`, `claws`, `walljump`

If the player has no starting items, they can use the attack button to "Meow" and alert nearby enemies.

### `levels` - Levels
Normally, this should be omitted or left blank as it will be filled in by the converted Ogmo Levels. However, if you have an external tool to convert levels, you can target the Ninja Cat Level Format and this property to have them pre-filled.

`basepak` is pre-filled, as there are no Ogmo-format levels for the original stages.

Pakify will skip packing Ogmo Levels for Regions with pre-filled levels. They will still be processed for size reduction and other changes, but no Ogmo levels will be added.
