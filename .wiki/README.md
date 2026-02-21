# Documentation for pakify

I've just written this here as GitHub does not allow Wikis on private repos.

Note: there are two versions of pakify:
- Integrated - is built into Ninja Cat Remewstered, and comes with a simple user-facing interface.
- Standalone (deprecated) - requires Python, but can be used in external workflows.

Steam Workshop support is planned, but is not implemented at the present time. Hold tight while I workshop (heh) a way to implement that.
- Please ignore any mentions of Steam Workshop in this Wiki as long as this notice exists.

## Contents

### Tutorials
- [Setup (pakify Integrated)](Setup%20Integrated.md)
- [Setup (pakify Standalone)](Setup%20Standalone.md) (deprecated)

### Properties and Templates
- [Ogmo Project](Ogmo%20Project.md)
- [Region Properties](Region%20Properties.md)
- [Set Properties](Set%20Properties.md)

### Extra Info
- [Tile Mechanics](Tile%20Mechanics.md)
- [Alternate Levels](Alternate%20Levels.md)
- [Modifier Considerations](Modifier%20Considerations.md)

## Developer Tools
To access the in-game Dev Menu, open the System Menu and go to `Options` > `Technical` > `Developer Tools`.

Here you can do various things, like hot-reload the level packs, grant yourself all upgrades, restore or set health, change modifiers, and so on. Most of these will only have a visible effect while in a level.

Continuing a Region after using this menu will place a marker on its score, so that you can still tell which scores are legitimate.

If you have access to a **Debug build**, the following are available:
- The Dev Menu is added to the base System Menu while in-game.
- `Tab` will rebuild and reload all level sets in-place.
- `[` and `]` skip between levels.
- `T` when held will force the touch layers to be shown.
- `Right Alt` toggles whether the UI layer is shown. This includes the in-game UI and all non-game screens, except the System Menu.
- `Left Alt` toggles whether the System Menu is hidden/disabled when in-game.
  - This allows the game to be paused without showing the System Menu, which is useful for screenshots.
- `Right Control` will step one frame when the game is paused. Again useful for screenshots, but also debugging frame-by-frame.
