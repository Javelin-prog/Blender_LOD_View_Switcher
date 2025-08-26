bl_info = {
    "name": "LOD Tools - LOD View Switcher",
    "author": "'AntiPoney' Jérôme Noël",
    "version": (1, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Header",
    "description": "Adds LOD switcher buttons in the viewport header",
    "category": "Import-Export",
    "doc_url": "https://github.com/AntiPoney/Blender_LOD_View_Switcher",
    "tracker_url": "https://github.com/AntiPoney/Blender_LOD_View_Switcher/issues",
}

import bpy
import os

# Register and Unregister
def register():
    
    from . import LOD_View_Switcher
    LOD_View_Switcher.register()

def unregister():
    
    from . import LOD_View_Switcher
    LOD_View_Switcher.unregister()

if __name__ == "__main__":
    register()