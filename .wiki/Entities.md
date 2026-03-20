# Entities

Some entities will activate when "hearing" noise nearby. Some actions are louder than others: e.g. a shuriken landing in wood is quieter than if it deflected off metal, and will activate entities in a smaller range.

## Player and Allies

### `start point` - Start Point
Marks where the player starts. There can be only one in a level.

You can change what entrance animation is used when starting the level here.

### `checkpoint` - Checkpoint
When the player enters its area, the level state is saved. Dying will respawn the player at the checkpoint's position. Checkpoints cannot be re-activated until a different checkpoint is activated.

Checkpoints are ignored when restarting the level and in Randomiser Mode.

### `rival npc` - Rival NPC
Executes a behaviour, then despawns. Variants are more-or-less self-explanatory, and control what animation sequence it plays.

Appears as Elenn by default, but when playing as her the Rival will use Ensy's sprites instead. Notes will refer to the Rival as Elenn going forward.

Can take damage in some animations, falling off the stage and interrupting the animation.
- e.g. in the `steal tile` animation, the player can hit Elenn with a weapon to prevent her from stealing the tile.

Interactions will modify the Rival Friendship value for the current playthrough:
- Attacking Elenn will reduce Friendship by 2.
  - Doing so after she fires a Bow for you will count doubly; this is betrayal.
- Letting Elenn do her thing will gradually raise Friendship, depending on the sequence playing.

Rival Friendship can be used to determine Alternates with the `Rival Friend` and `Rival Enemy` conditions. For example, a level late in the Region may change Elenn's behaviour and surrounding level design to assist or hinder the player depending on how they treated her in earlier stages.

### `bouldo` - Gold Rush Bouldo
Spawns automatically in Gold Rush mode, blocking the goal until all treasures are collected. Does nothing important otherwise, and may misbehave outside of Gold Rush. (untested)

### `cactuckey npc` - Cactuckey NPC
Scriptable NPC. Placing this object in Ogmo Editor provides a default example script where Cactuckey gets up when the player is near, and lays back down when the player is far.

Script format: `<command>;<next condition>`
- `command` format: `action:param`
- `next condition` format: `type:param`

`command`:
- `idle` - Regular idle animation. Faces player.
- `dead` - Grounded "dead" or unconscious animation.
- `getup` - Grounded getting up animation.
- `shock` - Shocked eyes.
- `apologise` - Bowing apologise animation. Faces player.
- `point` - Point in a direction. `point:left` or `point:right`.
- `loop` / `restart` - If final state, loops back to the first state. Otherwise NOOP.
- `cassette` - Set Cassette Block state: `cassette:<channel>:<state>` e.g. `cassette:red:on` or `cassette:green:off`

`next condition`:
- `time` / `t` - Proceed after specified frames. `action;time:60` to proceed from `action` after 1 second.
- `proximity` / `p` - Proceed when player is nearby. `action:proximity:32` to proceed when player is within 4 tiles (32px).
- `far` / `f` - Proceed when player is far away. `action:far:80` to proceed when player is at least 10 tiles (80px) away.
- `next` / `n` - Proceed to next state immediately. Useful with `cassette` action: `cassette:r:on;next` then `cassette:g:off` to swap Red and Green Cassette Blocks at once. (more-or-less)
- `stop` / `s` - Stop script here. Same effect as having no condition.

## Objects

### `sparkler` - Gem Cage
An electrified/spiky box that usually covers level goals. If it lands over a tile, it will remove it from the stage until defeated.

### `searchlight` - Searchlight
A beam of light which moves back and forth, where Variant defines the range of pixels to sweep over. Cycle offset can be adjusted.

Player can pass using a Sword Dash.

### `spotlight` - Spotlight
A beam of light.

Player can pass using a Sword Dash.

### `bomb dropper` - Bomb Dropper
Creates a `bomb` at a regular interval. Cycle offset can be adjusted: Higher value (0-1) makes it drop before others. Immune to all attacks.

Cycles faster in New Game Plus.

### `arrow shooter` - Arrow Shooter
Shoots an arrow sideways at a regular interval, direction dependent on flip. Cycle offset can be adjusted: Higher value (0-1) makes it shoot before others. Immune to all attacks.

Arrow can be parried with a Sword Dash, but this has no effect on the Arrow Shooter itself.

Cycles faster in New Game Plus.

### `plant` - Potted Plant
Mostly exists to look pretty. Leaves can block two Shuriken. Variant controls the style of plant, but has no effect gameplay-wise.

Sword can destroy leaves, and also cut the stem.

Chopping its stem with the leaves still on makes more noise than destroying them individually.

`whisk` variant is usually placed around level goals.

Variants `camellia`, `holly`, `lily` do not have final textures.

Flags can be set:
- Trapped: Spawns a bomb when the leaves are destroyed.
- Restorative: Does nothing.
- Gilded: Does nothing.

## Enemies

### `ninja` - Red Ninja
When hit or the player is seen, chases player. Can jump and go through platforms.

Takes extra damage if hit when idle.

In New Game Plus, they have more health.

### `shield ninja` - Armoured Ninja
Immune to most attacks. Shield can catch a shuriken.

When hit, walks slowly towards the player. Can fall through platforms.

Can be defeated with Bow.

### `demond` - Demond
A fake gem that usually covers level goals. If it lands over a tile, it will remove it from the stage until defeated.

These appear on gems that replace upgrades the player has already obtained.

In New Game Plus, they have more health and release a `demond ghost` when defeated.

### `magitsu` - Magitsu
Stands in place and casts magic fireballs that move towards the player's position at casting time. These do not travel through walls. Fireballs can be parried with Sword Dash and Shuriken.

Normally deals no contact damage. When low on health, enters "rabid mode" where they rapidly chase the player and deal contact damage.

In New Game Plus, they cast faster, enter "rabid mode" earlier, and have more health.

### `archer` - Archi
Stands in place and fires arrows at the player. These can stick to certain walls, and allow the player and other objects to bounce on them. Arrows can be parried with the Sword Dash.

Normally deals no contact damage. When low on health, enters "rabid mode" where they rapidly chase the player and deal contact damage.

In New Game Plus, they take significantly less time to reload, enter "rabid mode" earlier, and have more health.

### `durgen` - Flame Dragon
Unimplemented

Breathes fire.

### `bould dasher` - Bould Dasher
Unimplemented

Jumps to align with player. Can dash similarly to the Sword Dash, and can be parried.

Hitting with Sword or parrying:
- Throws the Bould Dasher away, but deals no damage.
- Parried Dasher is launched much faster, and will stick to walls.
- Player will bounce away, similarly to parrying Tiga.

### `bould jumper` - Bould Jumper
Jumps in place. Every few jumps, jumps higher.

### `bould roller` - Bould Roller
Unimplemented

Hops, then rolls rowards player. Does not stop until crashing into a wall, causing an explosion.

### `shuriken thrower` - Dragon Ninja
Unimplemented

Nimble dragon ninja. Shuriken can be deflected.

### `sworder` - Dragon Warrior
Unimplemented

Beefy dragon warrior. Can be parried.


## Bosses

### `boss 1` and `boss 2` - Tiga, The Last Tiger Ninja

Gained magic from the Kitsune-Tiger alliance. Spawn-relative movement. `boss 2` is effectively a `super` variant for `boss 1`; Tiga was implemented before Variants existed.

Summons Descending Spirits, uses Sword Dash, and casts Death Pillar spells. Tiga's Sword Dash can be parried with the player's Sword Dash.

It is not currently possible to program Tiga's behaviour through level data, and as such his patterns may not play well with custom arenas, especially if they allow the player to move far from the spawn point.

### `boss kitsu` - Kitsu, The Elder Kitsune

Uses magic fireballs and fire walls, as well as magic barriers. Level-relative movement. Variant `super` uses different attack patterns.

Fireballs can be parried with Sword Dash and Shuriken, and Fire Walls can be "parried" and passed through with a well-timed Sword Dash. 

Controls Cassette Blocks. (Red and Green channels)

Kitsu's behaviours and arenas were built to complement each other. It is not currently possible to program her behaviour through level data, and as such her patterns may not play well with custom arenas which aren't designed to match her default behaviours and block channel controls.

### `boss dago` - Dago, The Trial Dragon
Unimplemented

`super` variant uses a different, more difficult attack pattern.

### `boss bouldo` - Golden Alloy, The Greed-Bound Bould
Unimplemented

`super` variant uses a different, more difficult attack pattern.


## Projectile Entities

### `ghost` - Descending Spirit
Moves directly downwards, and despawns when it leaves the stage.

In New Game Plus, they move slightly toward the player as they descend.

### `demond ghost` - Chasing Spirit
Moves towards player with inertia, colliding with walls and platforms.

### `old ghost` - Chasing Spirit (legacy)
Moves towards player, slowing as it gets near, colliding with walls and platforms.

### `bomb` - Bomb
Falls, bounces, and explodes after a short delay. Explodes immediately when pierced by an arrow. Explosions only cover areas with line of sight to the bomb.

Creates a larger explosion in New Game Plus.

### `star` - Falling Shuriken
Falls and damages the player. Goes through tiles.


## Deprecated

### `bomb maker` - Bomb Dropper (legacy)
An older version of `bomb dropper`, retained for the original stages. Its cycle offset is determined by where it's placed, rather than being configurable.
