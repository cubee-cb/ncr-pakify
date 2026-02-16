# ncr-pakify

Documentation and resources for making Custom Levels for Ninja Cat Remewstered, using [Ogmo Editor 3](https://github.com/Ogmo-Editor-3/OgmoEditor3-CE).

Included is an Ogmo Project with all of the entities and tilesets already set up.

![screenshot of the ogmo editor next to ninja cat remewstered, editing one of its levels](.github/preview.png)

See [the wiki folder](.wiki) for [documentation](.wiki/README.md).

## Notes
- Workflows are untested on Windows, though they should work in theory. Feel free to help test!
- `.ncl` is short for Ninja Cat Level. A holdover from early development where each level was an individual file instead of being grouped in packs. They are just `json` files internally, but the extension makes it more obvious what the file is for.
- `basepak` might seem to contain no levels. This is because its `base.ncl` is pre-generated with all the levels included, made inside PICO-8 directly from the original game's map data rather than the Ogmo Project.
