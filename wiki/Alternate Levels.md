# Alternate Levels
For Standalone pakify, Alternate Levels are named in the following format: `<level>_<condition>.json`, like `1_goldRush.json`
- The important part is the `_`. That marks where the condition starts. You should only ever have ONE `_` in the filename.
- I would recommend following a format like `<index>-<name>_<condition>.json`, so `01-first-level_goldRush.json` or `03-pacifist-hallway_pacifism.json`, but as long as the levels are sorted as you like the only part of the name that matters is the condition.

For Integrated pakify, the filename is irrelevant; Alternates are instead described as part of the `order.json` file.

## Sorting Order (Integrated pakify)
Alternates will be appended to the previous listed level. That is, having the following `order.json`:
```json
[
  "first-stage.json",
    "goldrushing.json:goldRush",
    "pacifist-hall.json:pacifism",
  "second-stage.json"
]
```

puts `goldrushing.json` as the alternate of `first-stage.json` when Gold Rush Mode is active.

## Sorting Order (Standalone pakify)
Alternates will be appended to the last processed level. That is, having the following:

- `01.json`
- `02_goldRush.json`
- `03.json`

puts `02_goldRush` as an alternate of `01`, and `03` would be processed as Level 2:

- `01.json` - Level 1
- `02_goldRush.json` - Level 1 (Gold Rush alternate)
- `03.json` - Level 2

Adding a level sorted after `01` and before `02_goldRush` would change the flow again:

- `01.json` - Level 1
- `02.json` or `022.json` or `01a.json` - Level 2
- `02_goldRush.json` - Level 2 (Gold Rush alternate)
- `03.json` - Level 3

## Alternate Condition
Only one condition can be used at a time; the first alternate with a matching condition wins.

For example, if you have the Gold Rush and Pacifism modifiers enabled, but the Gold Rush Alternate appears first, the game would load the alternate level for Gold Rush Mode even when Pacifism Mode is enabled.

For Integrated, you can simply change the level order in `order.json` so the Pacifism Alternate appears first:
```json
[
  "first-stage.json",
    "pacifist-hall.json:pacifism",
    "goldrushing.json:goldRush",
  "second-stage.json"
]
```

For Standalone, you can guide pakify to process your alternates in a specific order by naming the file like `03a_pacifism.json` and `03b_goldRush.json`, as it processes them alphabetically. Do not add more `_`'s!
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
  - If your pack has any paths where the player may not obtain Double Jump, or has it early due to New Game Plus, you can check for that here.
- `hasClaws` and `notClaws` - Player has unlocked the Climbing Claws.
  - If your pack has any paths where the player may not obtain the Climbing Claws, or has them early due to New Game Plus, you can check for that here.
- `hasBow` and `notBow` - Player has or doesn't have the Bow weapon.
  - If your pack has any paths where the player may not obtain the Bow, or has it early due to New Game Plus, you can check for that here.
- `hasSword` and `notSword` - Player has or doesn't have the Sword weapon.
  - If your pack has any levels where the player may not have the Sword, but needs it (i.e. playing as Ensy), you can check for that here.
- `hasShuriken` and `notShuriken` - Player has or doesn't have the Shuriken weapon.
  - If your pack has any levels where the player may not have Shuriken, but needs them (i.e. playing as Elenn), you can check for that here.
