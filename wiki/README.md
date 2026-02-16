# Documentation for pakify

This is just here as GitHub does not allow Wikis on private repos.

Note: there are two versions of pakify:
- Standalone - This pakify requires Python, but can be used in external workflows.
- Integrated - This pakify is integrated into Ninja Cat Remewstered, and handles more convenience things.

Steam Workshop support is planned, but is not implemented at the present time. Hold tight while I workshop (heh) a way to implement that.
- Please ignore any mentions of Steam Workshop in this Wiki as long as this notice exists.

## Contents
- [Setup (pakify Standalone)](Setup.md)
- [Setup (pakify Integrated)](Setup-IntPakify.md)
- [Ogmo Project](Ogmo%20Project.md)
- [Base NCL Properties](Base%20NCL%20Properties.md)
- [Tile Mechanics](Tile%20Mechanics.md)
- [Modifier Considerations](Modifier%20Considerations.md)
- [Alternate Levels](Alternate%20Levels.md)

## Developer Tools
To access the in-game Dev Menu, open the System Menu and go to `Options` > `Technical` > `Dev Menu`.

Here you can do various things, like hot-reload the level packs, grant yourself all upgrades, restore or set health, and so on. Most of these will only have a visible effect while in a level.

Entering Score Submission after using this menu will place a marker on your score, so that you can tell which scores are legitimate.

If you have access to a Debug build, the following are available:
- The Dev Menu is added to the base Pause menu while in-game.
- `Tab` will reload level packs in-place.
- `[` and `]` skip between levels.
- `T` when held will force the touch layers to be shown.
- `Right Alt` toggles whether the UI layer is shown.
- `Left Alt` toggles whether the system menu is disabled when in-game.
  - This allows the game to be paused without showing the system menu, which is useful for screenshots.
- `Right Control` will step one frame when the game is paused.
