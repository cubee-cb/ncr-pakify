# Publishing to Steam Workshop:
Sets can only be published to the Steam Workshop using the Steam build of the game, while it is connected to Steam.
- To check if this is the case, either see if the Sets listed by Pakify have a Publish option, or check if the console output has `connected to steam!` followed by a greeting (e.g. `hello cubee!`) and that Steam hasn't lost connection.

## Workshop Metadata

You can set a preview image to show on the Workshop by adding `preview.png` next to your `set.json`. For consistency, I would suggest using the following guidelines:
- 32x32 canvas resolution, scaled up using Point, Nearest, or None filter to 256x256. Optional 2px border.
- Use the [PICO-8 Secret Colours palette](https://lospec.com/palette-list/pico-8-secret-palette).

This image can also be in `jpeg` format, but it has to have the `png` extension. I may change this in the future to detect more extensions.

You *can* set `title` and `description` in the `set.json`, but *these will overwrite any changes you make in Steam, if present, the next time you Publish.* This is more useful if you don't want to bother updating these fields through Steam after publishing.

## Publishing

Go to the Title Screen, open the System Menu, and select `Pakify`.
- Or from `Options` anywhere: `Options` > `Technical` > `Pakify`

![pakify root menu](images/pakroot.png)

Select the Level Set you want to publish, then select `Publish/Update set`.
- If the Level Set has already been published, it will be updated instead.
  - If the item was deleted from Steam Workshop, the game will attempt to create a new item instead.
- !! You will be returned to the title screen automatically when it finishes.

![pakify set menu](images/paksets.png)

![pakify publish button](images/pakpublish.png)

Pakify will build the Level Set and upload it to the Workshop using the details specified in `set.json`. This may take a few moments.
- The Set will have a `workshop.json` file added to its project folder. Do not remove or modify this unless you want to upload the Level Set again as a separate item.
- This will not build the pack to the Custom Levels folder; you will need to Pakify Build separately to update your local copy.
- If the upload fails, please check Troubleshooting below.

If the upload completes successfully, your new Workshop page will open in Steam.
- Here you can change the visibility of your Level Set. By default it will be set to Hidden, meaning other players cannot see it. Change this to Friends-only or Public when you're ready to share it with others!
- If you haven't set `title` and `description` in the `set.json`, you can update these through Steam. *Remember that if these fields are present, they will overwrite any changes you make in Steam the next time you Publish.*

## Troubleshooting

Common stuff:
- Double- and triple-check your files for incorrect filenames, missing commas or brackets, and general syntax errors.
- Try running Ninja Cat Remewstered through a console. This will provide detailed output about what exactly Pakify or the Level Set importer is failing on -> look for lines tagged with `[pakify]` or `[pakify (ERROR)]`.

### **Publish Failed!**

- Make sure your files are formatted correctly.
- Check that you have agreed to the Steam Subscriber Agreement / Workshop Terms of Service.

### **Pakify Failed!**

- Make sure your Regions have both `region.json` and `order.json`.

### **A level or alternate is missing!**

- Check `order.json` and ensure that you spelt its name and/or condition correctly.

### **What does "running through a console" mean?**

Please research "how to run applications through console linux/windows", it's fairly straightforward.
- For Windows, you would use CMD or PowerShell.
- For Steam Deck and other systems running KDE Plasma, it's most likely Konsole.
- For other Linux users, it depends on what exact flavour of Linux you have.

## `order.json` example
Format:
- `<filename>` - e.g. `epicLevel1.json`
- `<filename>:<alternate>` - e.g. `epicLevel1.json:pacifism`

The indentation here is optional; I use it to more easily tell which levels are Alternates.
```json
[
  "1.json",
  "2.json",
    "2-goldrush.json:goldRush",
  "3.json"
]

```
