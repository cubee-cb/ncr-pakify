# Modifier Considerations

## Guard Bell
The player may be able to "damage boost" through an otherwise difficult challenge by sacrificing hitpoints.

Try to avoid placing spikes on the bottom row of the world; the player will take damage from the spikes, then die from falling out of the world, losing two hitpoints when just the pit would have lost them only one.

## Gold Rush
All levels with multiple Goals are treated as if in Collectathon mode; players will need to collect ALL Goal Tiles before Bouldo will allow them to proceed.
- This is because there is canonically only one Bouldo; it makes sense lore-wise that he'd want all the gems collected as well, anyway.
  - "Bring me the seven Chaos Emeralds!"

Make sure players can backtrack so that they don't have to restart the level completely if they missed anything.

## Perfection / Pacifism
If your levels become near impossible with these modifiers, it might be worth loosening them up a little or creating [Alternates](Alternate%20Levels.md) so these modes are easier.

## New Game Plus
The player will start with the following Upgrades by default:
- Shuriken
- Sword
- Double Jump Scroll

You can set different starter upgrade for New Game Plus in the [Region Properties](Region%20Properties.md).

## Play As Elenn
Elenn has vastly altered physics;
- Much more slippery.
- Way faster maximum speeds.
- Longer Sword dash.
- Less powerful Shuriken throws, but are affected by movement speed.

In practice, she can do almost everything Ensy can, but it may be beneficial to make adjustments to cater to Elenn's physics.

## Invulnerability
Players can simply walk through all damage sources; the only things that cause the level to restart are Pits and Suffocation, or any "Miss" when combined with Perfection or Pacifism.

## Randomiser
The order of levels is randomised. The player can Restart Level to re-generate another level if the current one is impossible. Should never repeat a level.

Entities will be randomised within small groups of allowed replacements, and offset by a small, random amount horizontally.

Bosses will randomly replace each other.

## Dogblaster
Dogblaster is added to the starting items. It cannot activate Targets.

## Terra Guy
Terra Guy has really slow movement, and a shorter jump. However, he also starts with the Pickaxe Weapon, which can destroy any solid tile and build anywhere with empty space, so he can cheese pretty much any level.

The main blockage for Terra Guy is Spotlights combined with spike pits; he can't build or dig past the light at its wider points, and his short Sword Dash won't allow him to clear the other side of the spike pit.
