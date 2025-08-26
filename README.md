# Blender - LOD View Switcher

A Blender add-on for quickly switching Level of Detail (LOD) object visibility directly from the 3D Viewport header.

## Features

- Adds a row of LOD switcher buttons (`LOD0` → `LOD9`) in the 3D Viewport header  
- Toggle visibility of objects based on their name suffix (`_LODx`)
- Collapse/expand the entire LOD switcher group to save space in the header  
- Includes a `Show All` button to reveal every LOD object at once  

## Installation

1. Download the zip file from the [latest release](https://github.com/Javelin-prog/Blender_LOD_View_Switcher/releases/tag/stable-release)
2. Open Blender
3. Go to `Edit` > `Preferences` > `Add-ons` > `drop-down arrow`
4. Click `Install...` and select the ZIP file you downloaded
5. Enable the addon by checking the box

## location 

`3D Viewport` > `Top Header` > `LOD Switches`  

## Usage

1. Make sure your objects are named with the `_LODx` suffix (`_LOD0`, `_LOD1`, etc.)  
2. Use the LOD buttons in the viewport header to show only the objects that match the selected LOD level  
3. Press the `All` button to show all LOD objects regardless of suffix number  
4. Use the `< LODs Switches` / `> LODs Switches` toggle to expand or collapse the button group


## Notes

- The add-on only affects objects that follow the `_LODx` naming convention  
- It does not delete or modify geometry — only visibility is toggled

## License

MIT License
