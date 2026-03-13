# Basic Workflow
Usage of Ogmo Editor itself will not be covered here. It's a fairly simple program once you have the hang of it.

## Prerequisites
Place the `.ogmo` file and `.assets` folder from this repository into your Pakify Folder, like so:
- `pakify/`
  - `.assets/`
  - `ninja-cat-remewstered.ogmo`

These files are required for level creation and are not included with the game. To obtain them:
- Go to the main [GitHub Page](https://github.com/cubee-cb/ncr-pakify/).
- Click the green `Code` button and then `Download ZIP`.
- Place the ZIP file into the Pakify Folder, then extract it.
  - If the ZIP gets extracted into its own sub-folder, move its content back into the Pakify Folder.

## Steps
There is an example Level Set included in this repository under [`exampleSet`](../exampleSet).
- You can copy this folder directly into your Pakify Folder if you like, this can be used as a starting point.

### Making a new Level Set and/or Region:
- Go to the Level Pakify Folder.
- Create the Structure for your Level Set and/or Region.
  - See [Setup](Setup.md) for file structure.
  - See [Set Properties](Set%20Properties.md) and [Region Properties](Region%20Properties.md) for templates.

![a file browser inside a level set's folder](images/pakfolderset.png)

![a file browser inside a region's folder](images/pakfolderregion.png)

### Creating a Level for a Region:
- Open the Ogmo Editor, then press "Open Project" and find the `.ogmo` project file.
- Find the Region's folder, then right click it and press **Create Level Here**. Name it whatever you like.
  - Remember to add it into the Region's `order.json`. See [Alternate Levels](Alternate%20Levels.md) for replacing the level layout depending on the selected modifiers.

![image showing the previous steps in ogmo editor](images/ogmonew.png)

### Building your Level Set with Pakify:
- Open Ninja Cat Remewstered.
- Go to the Title Screen, open the System Menu, and select `Pakify`.
  - Or from `Options` anywhere: `Options` > `Technical` > `Pakify`

![pakify root menu](images/pakroot.png)

- Select the Level Set to run through Pakify, then select `Build`.
  - !! You will be returned to the title screen automatically when it finishes.

![pakify set menu](images/paksets.png)

![pakify build button](images/pakbuild.png)

![pakify success banner](images/pakok.png)

- Once complete, go to `New Game` in the main menu and see if your Regions are there.

![new game screen](images/paknewgame.png)

### Publishing to Steam Workshop:

See [Steam Workshop](Steam%20Workshop.md).

# Troubleshooting

Common stuff:
- Double- and triple-check your files for incorrect filenames, missing commas or brackets, and general syntax errors.
- Try running Ninja Cat Remewstered through a console. This will provide detailed output about what exactly Pakify or the Level Set importer is failing on -> look for lines tagged with `[pakify]` or `[pakify (ERROR)]`.

## **Pakify Failed!**

- Make sure your Regions have both `region.json` and `order.json`.

## **Region does not appear in the `New Game` menu**

- Make sure the Region files are formatted correctly, and `region.json` exists with valid content.

## **A level or alternate is missing!**

- Check `order.json` and ensure that you spelt its name and/or condition correctly.

## **Pakify doesn't see the Level Set!**

- Make sure it's in the Pakify Folder (**NOT** the Custom Levels folder) and contains a properly-formatted `set.json`.

## **What does "running through a console" mean?**

Please research "how to run applications through console linux/windows", it's fairly straightforward.
- For Windows, you would use CMD or PowerShell.
- For Steam Deck and other systems running KDE Plasma, it's most likely Konsole.
- For other Linux users, it depends on what exact flavour of Linux you have.
