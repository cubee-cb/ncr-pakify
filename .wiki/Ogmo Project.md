# Ogmo Project
This documents the properties accessible within the Ogmo Project File.

**Before you proceed**, there will be values available that may spoil potential future content. Whether these are or will be implemented in any current or future release of the game is not guaranteed, and any implementation of these values that exist now may change in the future.

## Layers

There are three layers read by Pakify:
- Entities
- Tiles
- Background Tiles

### Entities
The layout of objects that will spawn in the level. All entities can be used in any theme.

### Tiles
The base tilemap the player will interact with. The available tiles differ between level styles, so for your own sanity try to settle on a level theme before decorating your level.

### Background Tiles
These tiles are intangible, and serve as decoration only. Its theme can be chosen separately from the main Tiles layer, so you can mix and match decorations.

Solid tiles in the background layer will be rendered darker than other tiles. This is so decorative tiles can be stacked behind tangible tiles without being visually different from those placed in the foreground, while reducing confusion as to why otherwise solid tiles cannot be stood on.

## Level Properties
Right-click on the selected level in the sidebar, then click "Properties".

### Music
Select the background music to play during the level.
- `wind` - Ambient Wind
- `shuriken` - World 1 (Tiger Domain A)
- `last ninjacat` - World 2 (Tiger Domain B)
- `moss town` - World 3 (Kitsune Depths A) - missing
- `kitsune underpass` - World 4 (Kitsune Depths B)
- `eighty-six` - Tiga's boss track
- `trance of kitsu` - Kitsu's boss track
- `vaulter` - Vault Room theme
- `catwalk to victory` - Final Vault theme
- `chill` - Leaderboards theme
- `strange` - How To Play theme
- `sleepy` - A short and peaceful theme, originally from Marshmallow Infinity
- `snowflakes` - A cold but hopeful theme, created for Marshmallow Adventures (unreleased)
- `creepy night` - A weird, gloomy theme from Terra - A Terraria Demake (Forest Night)

The following are missing, but may be added in the future:
- `stilt town` - World 5 (Dragon Spires A)
- `dragon spires` - World 6 (Dragon Spires B)
- `land of greed` - Bouldo's region (Greed of Bouldo A)
- `trial of dago` - Dago's boss track
- `bouldos tantrum` - Bouldo's boss track
- `cactuckey cackle` - Cactuckey's boss track


### Background
`default` will use the background for the current level theme.
Set to anything other than `default` to use the background from that level theme:
- `Mountains` - Sky Mountains
- `MountainsTrees` - Sky Mountains with trees and houses.
- `Skyscrapers` - Office Buildings in the sky. Honestly, idk what 2020 me was thinking putting modern office buildings in a ninja game lol.
- `Forest` - Forest in front of mountains
- `Underground` - Underground Cavern

### Sky
Sky variant to use. Valid values:
- `night` - Blue night sky with moon.
- `underground` - Black sky with no moon or stars.
- `dawn` - An orange sky. Subject to change.
- `aurora` - Unfinished

### Fade Variant
Fade style to use when entering the level. Valid values:
- `cut` - Standard triangular fade pattern.
- `circle` - Large circle fade pattern. (Small circles in Old Style)
- `square` - Large square fade pattern. (Small squares in Old Style)
- `special` - Star fade. (Weird pattern in Old Style)

I usually use `special` for non-standard stages, such as:
- Upgrade Room.
- Boss Fight.
- Vault Room.
Basically, any stage that has a different pace or goal than others.

### Goal Mode
Changes how Goal tiles work. Valid values are the following:
- `normal` - The level ends when the player touches a Goal Tile.
  - This is the "standard" format for Ninja Cat levels. Reach the Goal Tile to finish.
  - If a level contains multiple Goal Tiles, only the one that the player touches will count: remember this if you have a Gem/Statue and an Upgrade in the same level, so the player doesn't softlock later if they lack the Upgrade.
- `collectathon` - The player must collect ALL Goal Tiles. (Gems, Statues, and Upgrades)
  - This will cause a "goals" counter to appear, much like Gold Rush's "bars" counter.
  - Upgrade Goals will grant the player the upgrade immediately when collected. You could use this to make metroidvania-like stages with backtracking.
  - This mode is forced if a stage with multiple Goal Tiles is entered in Gold Rush mode, since there is only one Bouldo and he can't logically be at all of the goals at once.
    - Bouldo will fly alongside the player until there is one Goal Tile remaining, then he will go sit on this Final Goal. This will reveal the direction it is located.
    - The Final Goal will be disabled completely if there is still Gold left in the stage. Touching it before Bouldo blocks it will only complete the stage if all of his requirements are met.
