# Pakify Documentation for Ninja Cat Remewstered

Documentation and resources for making Custom Levels for [Ninja Cat Remewstered](https://store.steampowered.com/app/4409630/Ninja_Cat_Remewstered/), using the integrated Pakify tool and [Ogmo Editor 3](https://github.com/Ogmo-Editor-3/OgmoEditor3-CE).

Included is an Ogmo Project with all of the entities and tilesets already set up, as well as the Vanilla Level Set containing the default levels.

![screenshot of the ogmo editor next to ninja cat remewstered, editing one of its levels](.github/preview.png)

See [the wiki folder](.wiki) for [documentation](.wiki/README.md).

## Notes
- `.ncl` is short for Ninja Cat Level. A holdover from early development where each level was an individual file instead of being grouped in packs. They are just `json` files internally, but the extension makes it more obvious what the file is for, and distinguishes them from unpacked Region Source files.
- `basepak` might seem to contain no levels. This is because its `region.json` is pre-generated with all the levels included, made inside PICO-8 directly from the original game's map data rather than the Ogmo Project.

Some things to keep in mind with regards to the different builds of the game:
- The native **Linux build** is what I would call the "first-class" build; this is the one I can test the most and will be supporting to the best of my ability.
  - Primarily because I run Linux, but also as Valve is investing heavily on Linux with the Steam Deck, Machine and such. Why not run natively on their hardware?
- The **Windows build** is secondary; I will attempt to support it as best I can, but as I do not use Windows as my main operating system help with any issues is limited.
  - As for *why* I made this game in Mono + C# when I'm not using Windows... I like MonoGame. I *started* development on Windows. That's about it.
- **Wine/Proton** are *NOT* supported; through limited testing I can confirm that the game at least runs, but any issues encountered that are exclusive to Wine/Proton will most likely not be worked on.
  - The game's data folders will be under the Windows path in `steamapps/compatdata/4409630/pfx/drive_c/users/steamuser/` or your Wine Prefix.
