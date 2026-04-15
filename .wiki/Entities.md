# Entities

Some entities will activate when "hearing" noise nearby. Some actions are louder than others: e.g. a shuriken landing in wood is quieter than if it deflected off metal, and will activate entities in a smaller range.

## Player and Allies

### `start point` - Start Point
Marks where the player starts. There can be only one in a level.

You can change what entrance animation is used when starting the level here.

### `bouldo` - Bouldo NPC
Spawns automatically in Gold Rush mode, blocking the goal until all treasures are collected.

If he does not have a saved tile set (i.e. when placed in a level manually), he will spawn a Bouldo Portal when approached instead of placing a Goal tile.

Variants are currently unused.

### `rival npc` - Rival NPC
Executes a behaviour, then despawns. Variants are more-or-less self-explanatory, and control what animation sequence it plays.

Appears as Elenn by default, but when playing as her the Rival will use Ensy's sprites instead. Notes will refer to the Rival as Elenn going forward.

Can take damage in some animations, falling off the stage and interrupting the animation.
- e.g. in the `steal tile` animation, the player can hit Elenn with a weapon to prevent her from stealing the tile.

Interactions will modify the Rival Friendship value for the current playthrough:
- Attacking Elenn will reduce Friendship by 2.
  - Doing so after she fires a Bow for you will count doubly; this is betrayal.
- Letting Elenn do her thing will gradually raise Friendship (typically by 1-2), depending on the sequence playing.

Rival Friendship can be used to determine Alternates with the `Rival Friend` and `Rival Enemy` conditions. For example, a level late in the Region may change Elenn's behaviour and surrounding level design to assist or hinder the player depending on how they treated her in earlier stages.

Her behaviour variants may be replaced in the future with Cactuckey's scripting.

### `cactuckey npc` - Cactuckey NPC
Scriptable NPC. Placing this object in Ogmo Editor provides a default example script where Cactuckey gets up when the player is near, and lays back down when the player is far.

Script format: `<command>;<next condition>`. For example:
- `idle;proximity:40` - Idle until the player enters a 40px radius.
- `cassette:red:on;next` - Set Red Cassette Blocks ON, then go to next action.
- `idle;far:80` - Idle until the player leaves an 80px radius.
- `cassette:red:off;next` - Set Red Cassette Blocks OFF, then go to next action.
- `loop` - Restart cycle.

`<command>` supports:
- `idle` - Regular idle animation. Faces player.
- `lookaway` - Faces player, with eyes averted.
- `trackeyes` - Eyes track player. Does not change facing direction.
- `dead` - Grounded "dead" or unconscious animation.
- `getup` - Grounded getting up animation.
- `shock` - Shocked eyes.
- `apologise` - Bowing apologise animation. Faces player.
- `blush` - Blushin animation with eyes averted. Faces player.
- `say:<n>` - Set speech bubble frame. `say:0` to turn speech bubble off.
- `point:<direction>` - Point in a direction. `point:left` or `point:right`.
- `loop` / `restart` - If final state, loops back to the first state. Otherwise NOOP.
- `cassette:<channel>:<state>` - Set Cassette Block state. e.g. `cassette:red:on` or `cassette:green:off`
- `removecamfocus` - Deletes the object overriding camera focus. Useful when there is a Camera Focus Area over a room Cactuckey is to un-focus the room when his animation finishes.

`<next condition>` supports:
- `time:<frames>` / `t:<frames>` - Proceed after specified frames. `action;time:60` to proceed from `action` after 1 second.
- `proximity:<px>` / `p:<px>` - Proceed when player is nearby. `action:proximity:32` to proceed when player is within 4 tiles (32px).
- `far:<px>` / `f:<px>` - Proceed when player is far away. `action:far:80` to proceed when player is at least 10 tiles (80px) away.
- `next` / `n` - Proceed to next state immediately, identical to `time:0`. Useful with `cassette` action: `cassette:r:on;next` then `cassette:g:off` to swap Red and Green Cassette Blocks at once. (more-or-less)
- `stop` / `s` - Stop script here.

## Areas

### `dynamic goal` - Dynamic Goal
Allows the player to complete the stage without collecting a Gem or Upgrade.

Variants:
- `portal` - Bouldo's portals. Bouldo will spawn this if he does not have a saved tile.
- `gizmo` - Rainbow goal portal from Fire Dino.
- `cactuckey` - Cactuckey. Hovers then flies away.
- `basic` - Default portal. Green circle.

Variants may have different delays before completing the stage, to give time for their animations to play.

If present while Collectathon Mode or Gold Rush Mode are active, all Dynamic Goals will close and only open when all regular Goals are collected. Useful to create one or many dedicated exit points for these stages.

### `checkpoint` - Checkpoint
When the player enters its area, the level state is saved. Dying will respawn the player at the checkpoint's position. Checkpoints cannot be re-activated until a different checkpoint is activated.

Checkpoints are ignored when restarting the level and in Randomiser Mode.

### `camera pan area` - Camera Pan Area
While the player is within its area, the camera will pan, similar to Camera Pan Tiles.

Variant acts as a multiplier for how far the camera will pan (set negative to pan left). Panning is most effective at Original resolution, and lowers in strength as the resolution widens.

### `camera focus area` - Camera Focus Area
While the player is within its area, the camera will detach from the player and focus on this object. (note the `Focus!` point on its visual is the centre)

The area is about the same as the minimum internal resolution, so everything inside it is guaranteed to be visible while focused.

*yeah, it's a Mesmeriser reference. shush.*


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

Falls and breaks when unsupported above. Level Upper Bound counts as support.

### `arrow shooter` - Arrow Shooter
Shoots an arrow sideways at a regular interval, direction dependent on flip. Cycle offset can be adjusted: Higher value (0-1) makes it shoot before others. Immune to all attacks.

Arrow can be parried with a Sword Dash, but this has no effect on the Arrow Shooter itself.

Cycles faster in New Game Plus.

Falls and breaks when unsupported behind.

### `plant` - Potted Plant
Mostly exists to look pretty. Leaves can block two Shuriken. Variant controls the style of plant, but has no effect gameplay-wise.

Sword can destroy leaves, and also cut the stem.

Chopping its stem with the leaves still on makes more noise than destroying them individually.

`whisk` variant is usually placed around level goals to signal the level end and as a "valuable" decoration.

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

Planned: Breathes fire.

### `bould dasher` - Bould Dasher
Unimplemented

Planned: Jumps to align with player. Can dash similarly to the Sword Dash, and can be parried.

Planned: Hitting with Sword or parrying:
- Throws the Bould Dasher away, but deals no damage.
- Parried Dasher is launched much faster, and will stick to walls.
- Player will bounce away, similarly to parrying Tiga.

### `bould jumper` - Bould Jumper
Jumps in place. Every few jumps, jumps higher.

### `bould roller` - Bould Roller
Unimplemented

Planned: Hops, then rolls rowards player. Does not stop until crashing into a wall, causing an explosion.

### `shuriken thrower` - Dragon Ninja
Unimplemented

Planned: Nimble dragon ninja. Shuriken can be deflected.

### `sworder` - Dragon Warrior
Unimplemented

Planned: Beefy dragon warrior. Can be parried to defeat quickly.


## Bosses

### `boss tiga` - Tiga, The Last Tiger

Uses a sword alongside magic gained from an alliance with the Kitsune. Spawn-relative movement.

Uses different attack patterns with variant `super` and/or in New Game Plus.

Summons Descending Spirits, uses Sword Dash, and casts Death Pillar spells. Tiga's Sword Dash can be parried with the player's Sword Dash.

It is not currently possible to program Tiga's behaviour through level data, and as such his patterns may not play well with custom arenas, especially if they allow the player to move far from the spawn point.

Set `savedTile` to specify a specific tile ID to drop when defeated.

### `boss kitsu` - Kitsu, The Eldest Kitsune

Casts magic fireballs and fire beams, as well as magic barriers (represented in-game using Cassette Blocks). Level-relative movement.

Uses different attack patterns with variant `super` and/or in New Game Plus.

Fireballs can be parried with Sword Dash and Shuriken, and Fire Walls can be "parried" and passed through with a well-timed Sword Dash. 

Controls Cassette Blocks. (Red and Green channels)

Kitsu's behaviours and arenas were built to complement each other. It is not currently possible to program her behaviour through level data, and as such her patterns may not play well with custom arenas which aren't designed to match her default behaviours and block channel controls.

Set `savedTile` to specify a specific tile ID to drop when defeated.

### `boss dago` - Dago, The Trial Dragon
Unimplemented. Intangible

### `boss bouldo` - Golden Alloy, The Greed-Bound Bould
Unimplemented. Can be defeated.

Drops Region Trophy instead of a Gem by default, and never drops Bouldo in Gold Rush mode.

Set `savedTile` to specify a specific tile ID to drop when defeated.


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
An older version of `bomb dropper`, retained for the original stages. Its cycle offset is determined by where it's placed, rather than being configurable, and its other behaviour is more or less identical.

