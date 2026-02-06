# Ogmo Project

## Level Properties
Right-click on the selected level in the sidebar, then click "Properties".

### Music
Select the background music to play during the level.
- `wind` - Ambient Wind
- `sneaking` - World 1
- `last ninjacat` - World 2
- `moss town` - World 3, missing
- `kitsune underpass` - World 4
- `eighty-six` - Tiga's Boss Theme
- `trance of kitsu` - Kitsu's Boss Theme
- `chill` - Leaderboards Theme
- `vaulter` - Vault Rooms
- `catwalk to victory` - Final Vaults (Region End)
- `strange` - A goofy and confusing theme
- `snowflakes` - A cold but hopeful theme
- `sleepy` - A short and peaceful theme

The following are missing, but may be added in the future:
- `stilt town` - World 5
- `dragon spires` - World 6
- `land of greed` - Bouldo's Region
- `trial of dago` - Dago's Boss Theme
- `bouldos tantrum` - Bouldo's Boss Theme
- `cactuckey cackle` - Cactuckey's Boss Theme


### Background
`default` will use the background for the current level theme.
Set to anything other than `default` to use the background from that level theme:
- `world1` - Sky Mountains
- `world2` - Sky Mountains with trees and houses. (Skyscrapers in Old Style)
- `world3` - Forest
- `world4` - Underground Cavern

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
- `normal` - The level ends when the player collects a Goal Tile.
- `collectathon` - The player must collect ALL Goal Tiles (Gems, Statues, and Upgrades) to complete the level.
  - This will cause a "goals" counter to appear, much like Gold Rush's "bars" counter.
  - This mode is forced if a stage with multiple goals is entered in Gold Rush mode, since there is only one Bouldo, and for lore reasons he can't block all the goals.
