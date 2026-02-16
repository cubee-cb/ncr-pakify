# Base NCL Properties
## Template

```
// base.ncl template
{
  "id": "template",
  "requireGameVersion": 1, // v1.2mg
  "unlocked": true,
  "hidden": false,

  "displayName": {
    "english": "template",
    "meowlang": "meow"
  },
  "description": {
    "english": "a template ripe for editing!",
    "meowlang": "meow meow meow"
  },

  // menu details
  "glyph": "202000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000dddddddd0000000000000000000000ddd677776ddd0000000000000000000dd6777777776dd00000000000000000dd677777737776dd0000000000000000d67777773337776d000000000000000dd777777bb377777dd00000000000000d677777bbb7777776d00000000000000d677773bb77777776d00000000000000d6777b33777777776d00000000000000d6677bbddddd77766d00000000000000d6667777777777666d00000000000000d7666677777766667d00000000000000dd66666666666666dd000000000000000d76666666666667d0000000000000000dd766666666667dd00000000000000000dd7766666677dd0000000000000000000ddd777777ddd0000000000000000000000dddddddd00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
  "worldTheme": "world1",
  "worldSky": "night",
  "worldFade": "cut",

  "rewards": [],
  "newGamePlusItems": [],

  "levels": []

}
```

## Properties

### `id` - Identifier
Used internally for scoreboards, save files, and the like. This is not typically visible to the player. (see `displayName` and `description`)

When choosing an `id`, try to think of something unique to avoid conflicting with other people's Packs. A good idea might be to include your username with it, or add some random words:
- `NinjaCatPlayer UltraChallengePack`
- `doomcastle by creampuff`
- `kaizo observatory - charlise hopscotch`
- `orangejuice ledgehop inmost magicat`

If the game tries to load a pack with an `id` that is already taken, the new pack will be skipped and a warning popup will be shown.
- In `save.json`, you can set it to replace loaded Packs instead and/or turn off the warning popups. (for example, if you're editing the Vanilla Packs)

### `displayName` - Name of the Pack
Shown in the New Game menu under the Pack Glyph.
Contains a Dictionary of language keys, with corresponding text.

Each line of this label fits 16 characters, so keep these names reasonably short.

### `description` - Short Description.
Shown in the New Game menu at the top of the screen.
Contains a Dictionary of language keys, with corresponding text.

Descriptions can be longer than the Display Name, but try to keep them within 32-64 characters.

### `author` - Creator of the Pack.
Currently unused.
May be a User ID for Steam Workshop Uploads.

### `revision` - Version of the Pack.
Currently unused.
May be used for Steam Workshop or removed in the future.

### `requireGameVersion` - Minimum Game Version
This field is also part of `set.json`; this one can be used if you have only some Regions that require a newer version, but others will work on a lower version.

Valid Values:
- `0` - Any Version
- `1` - v1.2mg - Region Packs introduced.

`0` and `1` are interchangeable.

Packs made for a newer version of the game will not be loaded, and a notification will be displayed informing the user to update their game.

### `unlocked` - Unlocked by Default
Set this to `false` if you would like this pack to be locked initially.

This pack can then be added as a `reward` for completing a different pack, for example as part of a larger campaign.

### `hidden` - Hide when Locked
Set this to `true` if you would like this pack to be hidden until it is unlocked; it will not appear in the menus, nor the leaderboards. Good for "secret" regions.

Unlocking a hidden pack will display alternative unlock text, saying that a **secret region** was found.

### `glyph` - Pack Glyph
The `glyph` property expects a string in the PICO-8 gfx string format. It will be shown in the New Game and Leaderboard menus alongside the other packs.
Glyphs can be made inside PICO-8 and copy-pasted directly from the sprite editor to the text file. (the web-based [Education Edition](https://www.pico-8-edu.com/) works fine for this use case)
- Omitting/removing the pack glyph will result in a generic icon being used. If you want your pack to be easily recognisable, make sure to give it a cool icon!

Typical glyph size is 16x16px plus a 1px border, drawn in the centre of a 32x32px sprite.

```
// pico-8 sprite string format
// WW HH are the sprite Width and Height, in hex (e.g. 1010 for a 16x16 sprite)
// xxxx is the piXel data, in hex
// [gfx]WWHHxxxxxxxxxxxxxxxx[/gfx]

// used as a pack glyph (note the [gfx] tags are optional)
  "glyph": "[gfx]WWHHxxxxxxxxxxxxxxxx[/gfx]",
  "glyph": "WWHHxxxxxxxxxxxxxxxx",
```

Pack Glyphs can be up to 128x128px in size (the same size as the PICO-8 spritesheet)

### `worldTheme` - Background
World background to use on the pack's leaderboard page. Valid values:
- `world1` - Sky Mountains
- `world2` - Sky Mountains with trees and houses. (Skyscrapers in Old Style)
- `world3` - Forest
- `world4` - Underground Cavern

### `worldSky` - Sky
Sky variant to use on the pack's leaderboard page. Valid values:
- `night` - Blue night sky with moon.
- `underground` - Black sky with no moon or stars.
- `dawn` - An orange sky. Subject to change.
- `aurora` - Unfinished

### `worldFade` - Fade Style
Fade style to use on the pack's leaderboard page. Valid values:
- `cut` - Standard triangular fade pattern.
- `circle` - Large circle fade pattern. (Small circles in Old Style)
- `square` - Large square fade pattern. (Small squares in Old Style)
- `special` - Star fade. (Weird pattern in Old Style)

### `rewards` - Pack-completion Rewards
Format: `<type>:<item>` or `<condition>;<type>:<item>`

These allow you to unlock certain things for the player when they complete your level pack.

Valid items for type `modifier`:
- `new game plus` - Unlock "New Game Plus" mode.
- `ln` - Unlock "Play As Elenn" mode.

Valid items for type `region`:
- The `id` of any Region Pack. If the pack isn't loaded, this will be done without creating the notification.

Valid for `condition`:
- `guard bell` - Unlock only if Guard Bell is active.
- `gold rush` - Unlock only if Gold Rush is active.
- `one life` - Unlock only if One Life is active.
- `perfection` - Unlock only if Perfection Mode is active.
- `pacifism` - Unlock only if Pacifism Mode is active.
- `new game plus` - Unlock only if New Game Plus is active.
- `ln` - Unlock only if playing as Elenn.

Example:
```
  "rewards": [
    "region:sequel", // unlock pack "sequel"
    "modifier:new game plus", // unlock New Game Plus mode
    "gold rush;region:bouldo" // unlock pack "bouldo" if beaten with Gold Rush enabled
  ],
```

### `newGamePlusItems`
A list of items to grant the player in New Game Plus mode.

Example of all valid values:
```
  "newGamePlusItems": [
    "shuriken",
    "sword",
    "bow",
    "double jump",
    "climbing claws"
  ],
```

When not specified, New Game Plus grants the following items:
- Shuriken
- Sword
- Double Jump

### `levels` - Levels
Normally, this should be left blank as it will be filled in by `pakify`.

`basepak` is pre-filled, as there are no Ogmo-format levels for the original stages.
