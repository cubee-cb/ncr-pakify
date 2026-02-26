# Set Properties
## Template

```json
{
  "id": "level set",
  "author": "author",
  "revision": 1,
  "requireGameVersion": 1,
  "regions": [
    "region1",
    "region2"
  ]
}
```

## Properties

### `id` - Identifier
Not visible to the player. Used for debugging output.

### `title` - Steam Workshop Title (optional)
Optionally sets the title of the Level Set when published to the Steam Workshop.

If you edit the title through Steam, omit this property. Re-uploading the pack will overwrite any changes if this property exists.

### `description` - Steam Workshop Description (optional)
Optionally sets the description of the Level Set when published to the Steam Workshop.

If you edit the description through Steam, omit this property. Re-uploading the pack will overwrite any changes if this property exists.

### `author` - Creator of the Set
Currently unused.

### `revision` - Version of the Set
Currently unused.

### `requireGameVersion` - Minimum Game Version
Valid Values:
- `0` - Any Version
- `1` - v1.2mg - Custom Levels introduced.

`0` and `1` are interchangeable.

Level Sets made for a newer version of the game will not be loaded, and a notification will be displayed informing the user to update their game.

### `regions` - List of regions to include in this Set
Used by pakify to determine what Regions to build, and by the game to determine which Regions to load.

Put the **folder name** of each Region here, *NOT* the `id`.
