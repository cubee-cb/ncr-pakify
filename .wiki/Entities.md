# Entities

## Player and Allies

### `start point` Start Point
Marks where the player starts. There can be only one in a level.

### `checkpoint` Checkpoint
When the player enters its area, the level state is saved. Dying will respawn the player at the checkpoint's position.

Restarting the level ignores checkpoints.

### `elenn npc` Elenn NPC
Executes a behaviour, then despawns. Variants are more-or-less self-explanatory.

Can take damage, falling off the stage and interrupting the animation.

### `bouldo` Gold Rush Bouldo
Spawns automatically in Gold Rush mode, blocking the goal until all treasures are collected. Does nothing important otherwise.

## Objects

### `sparkler` Gem Cage
An electrified/spiky box that usually covers level goals. If it lands over a tile, it will remove it from the stage until defeated.

### `searchlight` Searchlight
A beam of light which moves back and forth in a definable range of pixels.

Player can pass using a Sword Dash.

### `spotlight` Spotlight
A beam of light.

Player can pass using a Sword Dash.

### `bomb dropper`
Creates a `bomb` at a regular interval. Cycle offset can be adjusted: Higher value (0-1) makes it drop before others.

Can be damaged with the Sword. (think of it like, prying it off the roof)

Cycles faster in New Game Plus.

### `arrow shooter`
Shoots an arrow sideways at a regular interval, direction dependent on flip. Cycle offset can be adjusted: Higher value (0-1) makes it shoot before others.

Arrow can be parried, destroying the Arrow Shooter.

Cycles faster in New Game Plus.

### `plant`
Mostly exists to look pretty. Leaves can block two Shuriken.

Sword can destroy leaves, and also cut the stem.

Chopping stem with the leaves still on makes more noise than destroying them individually.

`whisk` variant is usually placed around level goals.

## Enemies

### `ninja` Red Ninja
When hit or the player is seen, chases player. Can jump and go through platforms.

Takes extra damage if hit when idle.

In New Game Plus, they have more health.

### `shield ninja` Armoured Ninja
Immune to most attacks. Shield can catch a shuriken.

When hit, walks slowly towards the player. Can fall through platforms.

Can be defeated with Bow.

### `demond` Demond
A fake gem that usually covers level goals. If it lands over a tile, it will remove it from the stage until defeated.

These appear on gems that replace upgrades the player has already obtained.

In New Game Plus, they have more health and release a `demond ghost` when defeated.

### `magitsu` Magitsu
Stands in place and casts magic fireballs that chase the player. These do not travel through walls.

No contact damage.

When low on health, enters "rabid mode" where they rapidly chase the player and deal contact damage.

In New Game Plus, they cast faster, enter "rabid mode" earlier, and have more health.

### `archer` Archi
Stands in place and fires arrows at the player. These can stick to some walls, and allow the player and other objects to bounce on them.

No contact damage.

When low on health, enters "rabid mode" where they rapidly chase the player and deal contact damage.

In New Game Plus, they take less time to reload, enter "rabid mode" earlier, and have more health.

### `aaaaaaaa`
aaaaaaaaa

### `aaaaaaaa`
aaaaaaaaa

### `aaaaaaaa`
aaaaaaaaa

## Bosses

### `boss 1` and `boss 2` Tiga
The Last Tiger Ninja.

Gained magic from the Kitsune-Tiger alliance. Spawn-relative movement.

Summons spirits, uses sword dash, and casts death spells.

### `boss kitsu` Kitsu
Elder Kitsune.

Uses magic fireballs and fire walls, as well as magic barriers. Level-relative movement.

Controls Cassette Blocks (Red and Green)

### `boss dago` Dago - Unimplemented
Trial dragon.

### `boss bouldo` Golden Bouldo - Unimplemented
Greed-molten Bould.


## Projectile Entities

### `ghost`
Moves directly downwards, and despawns when it leaves the stage.

In New Game Plus, they move slightly toward the player as they descend.

### `old ghost`
Moves towards player, slowing as it gets near, colliding with walls and platforms.

### `demond ghost`
Moves towards player with inertia, colliding with walls and platforms.

### `bomb`
Falls, bounces, and explodes after a short delay. Explodes immediately when pierced by an arrow.

Creates a larger explosion in New Game Plus.

### `star`
Falls and damages the player. Goes through tiles.

## Unimplemented

### `durgen`
Breathes fire.

### `bould dasher`
Can dash similarly to the sword dash. Jumps to align with player. Parries throw it away, but deal no damage.

### `bould jumper`
Jumps in place. Every few jumps, jumps higher.

### `bould roller`
Hops, then rolls rowards player. Does not stop until crashing into a wall, causing an explosion.

### `shuriken thrower`
Nimble dragon ninja. Shuriken can be deflected.

### `sworder`
Beefy dragon warrior. Can be parried.

## Deprecated

### `bomb maker`
An older version of `bomb dropper`, retained for the original stages. Its cycle offset is determined by where it's placed, rather than being configurable.
