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

### `author` - Creator of the Pack.
Currently unused.
May be a User ID for Steam Workshop Uploads.

### `revision` - Version of the Pack.
Currently unused.
May be used for Steam Workshop or removed in the future.

### `requireGameVersion` - Minimum Game Version
Valid Values:
- `0` - Any Version
- `1` - v1.2mg - Region Packs introduced.

`0` and `1` are interchangeable.

Level Sets made for a newer version of the game will not be loaded, and a notification will be displayed informing the user to update their game.
