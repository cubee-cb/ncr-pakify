# Tile Mechanics

## Channels and Colours
There are two Channels in Ninja Cat: Red and Green.

When using elements related to these Channels, the following non-colour visual identifiers are also used:

Red:
- Elements in Ones (one band across doors)
- Bullseye Target
- Outlines

Green:
- Elements in Twos (two bands across doors)
- Dot Target
- Filled Shapes
- Vines or Lights

## Platforms
Depending on their Platform Safety setting, the player may not be able to fall directly through platforms. Keep this in mind if you have any segments where the player needs to fall through platforms quickly.

Removable platforms are considered solid, instead of as proper platforms, as they are sometimes used as Doors.

## Targets
Hitting these with any weapon, or headbutting them, will activate them.

Red Targets:
- Open Red Door tiles in their current and adjacent columns.
- Toggle all Red Cassette Blocks.

Green Targets:
- Open Green Door tiles across the entire level.
- Open Removable Platform tiles across the entire level.
- Toggle all Green Cassette Blocks.

## Falling Tiles
Falling Tiles fall to the ground when a supporting tile is removed. If an entity or the player is contained within one and cannot be ejected, it will be killed. (excluding other Falling Tiles)

These tiles will not fall if placed directly in the air; only when a tile below them is removed.

Falling Tiles are technically entities. Like other entities, Falling Tiles will bounce on Wall Arrows, and they will hurt the player if they collide.

## Cassette Blocks
Cassette Blocks are toggleable. If an entity or the player is contained within one when it turns solid and cannot be ejected, it will be killed. (excluding Falling Tiles)

Currently these blocks are toggled by the corresponding target colour, and turned on or off directly by Boss Kitsu.

Why "Cassette Blocks" and not, like, Toggle Blocks?:
- Named after the Cassette areas in Celeste, for the similar toggling behaviour of blocks. *looks it up - oh wait they genuinely are just called cassette blocks in celeste as well lol*
- Also a play on [Cassette Fox](https://cubee.games/wiki/?cat=characters&page=misc#cassette)'s name.

## Climbable Tiles
Some tiles can be climbed when the player has Climbing Claws. (this is always the case in New Game Plus)

Typically, tiles that shuriken can stick to are climbable, but there are some exceptions. Consider the following:
- Materials that have **small ridges** or are otherwise **grippable** are climbable. This includes **hard** materials like World 1's Wood or World 3's Tiles and Mossy Bricks.
  - **Little/no** impaling force required.
- Materials that are **stabbable** can hold shuriken and arrows, but may not be climbable. This is usually **softer** materials like World 2's Brick Trims or World 4's Dirt.
  - **High** impaling force required.

## Spikes
Spikes will damage the player when fallen onto from above. Wall Spikes currently have somewhat broken collisions and may not work as expected.

Players can walk through spikes horizontally without harm, similarly to Spelunky.

## Goals
Upgrade Goals will be replaced with Gems when the upgrade is already owned.

About the Dogblaster and Pickaxe Goals:
- These will also be replaced with Gems if their respective modifiers aren't unlocked, keep this in mind if making a level dependent on them.
- You can still grant these as `startingItem`s -> add `"dog"` or `"tool"`.
- Obtaining these Upgrades in any way other than through the intended unlocks (i.e. starting items, save editing) will not unlock the modifiers, nor grant any achievements.
