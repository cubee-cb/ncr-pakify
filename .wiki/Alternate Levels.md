# Alternate Levels
Alternates are described as part of the `order.json` file.

## Alternate Condition
Alternate Conditions are case-insensitive and can contain spaces. All of the following and more should work:
- `goldRush`, `GOLD RUSH`, `gold rush`, `Go L dRu S h`

You can combine multiple conditions by separating them with commas. For example, for an Alternate that appears only in New Game Plus, and another that appears in Gold Rush + Pacifism:
```json
[
  "first-stage.json",
    "pacifist-hall.json: new game plus",
    "goldrushing.json: gold rush, pacifism",
  "second-stage.json"
]
```

Modifiers don't have to match the conditions exactly; as long as all conditions are met, the Alternate will be used.
- For example, if you're playing **Gold Rush + One Life**, the **Gold Rush** alternate will be used if there is no dedicated **Gold Rush + One Life** alternate. However, a **Gold Rush + One Life** alternate will never be used when only **Gold Rush** is active *without* **One Life**.

Valid alternates are the following (case insensitive):
- `Pacifism` - Pacifism modifier is enabled.
  - I use this to replace the boss fights with vault rooms, which usually try teaching niche mechanics like how hitting a Shield Ninja's shield with shuriken will not kill the player, or otherwise as small puzzle rooms.
- `Perfection` - Perfection modifier is enabled.
  - Maybe your level is really precise. You can make an alternate to make it easier to not make a mistake.
- `Guard Bell` - Guard Bell modifier is enabled.
  - Maybe you want to prevent people from cheesing your level. You could make an alternate tailored for Guard Bell's hitpoint system? Or troll them, idk it's up to you.
- `Gold Rush` - Gold Rush modifier is enabled.
  - You could use this to add extra gold or an alternative layout to make gold the main focus of the level.
- `New Game Plus` - New Game Plus modifier is enabled.
  - Add more enemies, make tighter jumps, smaller platforms, it's up to you. Or subvert people's expectations and make it easier?
- `Elenn` and `Not Elenn` - Playing as Elenn or not.
  - This can be used to make challenges tailored for Elenn's faster, more slippery movement.
- `Has Double Jump` and `Not Double Jump` - Player has unlocked Double-Jump.
  - If your pack has any paths where the player may not obtain Double Jump, or has it early due to New Game Plus, you can check for that here.
- `Has Claws` and `Not Claws` - Player has unlocked the Climbing Claws.
  - If your pack has any paths where the player may not obtain the Climbing Claws, or has them early due to New Game Plus, you can check for that here.
- `Has Bow` and `Not Bow` - Player has or doesn't have the Bow weapon.
  - If your pack has any paths where the player may not obtain the Bow, or has it early due to New Game Plus, you can check for that here.
- `Has Sword` and `Not Sword` - Player has or doesn't have the Sword weapon.
  - If your pack has any levels where the player may not have the Sword, but needs it (e.g. playing as Ensy), you can check for that here.
- `Has Shuriken` and `Not Shuriken` - Player has or doesn't have the Shuriken weapon.
  - If your pack has any levels where the player may not have Shuriken, but needs them (e.g. playing as Elenn), you can check for that here.
- `Rival Friend` - Player hasn't attacked the Rival enough times. (`friendship >= 4`)
  - Use this if you want to tell a behaviour-driven story about friendship between Elenn and Ensy.
- `Rival Enemy` - Player has attacked the Rival too much. (`friendship <= -2`)
  - Use this if you want to tell a behaviour-driven story about conflict between Elenn and Ensy.

## Sorting Order
Alternates will be appended to the previous listed level. That is, having the following `order.json`:
```json
[
  "first-stage.json",
    "goldrushing.json: gold rush",
    "pacifist-hall.json: pacifism",
  "second-stage.json"
]
```

will put `goldrushing.json` as the alternate of `first-stage.json` when in Gold Rush Mode, and `pacifist-hall.json` as the alternate when in Pacifism Mode.

I personally like to indent Alternates so I can see where they are more easily, this is optional.
