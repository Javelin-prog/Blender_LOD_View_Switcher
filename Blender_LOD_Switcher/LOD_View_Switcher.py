import bpy
import re

# Regex to detect _LOD#
lod_pattern = re.compile(r".*_LOD(\d+)$")

def show_all_lods():
    """Unhide all LOD objects"""
    for obj in bpy.data.objects:
        match = lod_pattern.match(obj.name)
        if match:
            obj.hide_set(False)
            obj.hide_viewport = False

def set_lod_visibility(target_lod):
    for obj in bpy.data.objects:
        match = lod_pattern.match(obj.name)
        if match:
            lod_num = int(match.group(1))
            obj.hide_set(lod_num != target_lod)
            obj.hide_viewport = (lod_num != target_lod)

# Operator for switching LOD
class OBJECT_OT_set_lod(bpy.types.Operator):
    bl_idname = "object.set_lod_header"
    bl_label = "Set LOD"
    bl_description = "Switch object visibility based on LOD"

    lod_value: bpy.props.IntProperty()

    def execute(self, context):
        context.scene.active_lod = self.lod_value
        set_lod_visibility(self.lod_value)
        return {"FINISHED"}

# Toggle collapse/expand
class OBJECT_OT_toggle_lod_buttons(bpy.types.Operator):
    bl_idname = "object.toggle_lod_buttons"
    bl_label = "Toggle LOD Buttons"
    bl_description = "Expand/Collapse LOD Switcher buttons"

    def execute(self, context):
        context.scene.lod_buttons_expanded = not context.scene.lod_buttons_expanded
        return {"FINISHED"}
    
# Operator for "Show All"
class OBJECT_OT_show_all_lods(bpy.types.Operator):
    bl_idname = "object.show_all_lods"
    bl_label = "Show All LODs"
    bl_description = "Show all objects with LOD suffixes"

    def execute(self, context):
        context.scene.active_lod = -1
        show_all_lods()
        return {"FINISHED"}

# Draw in 3D Viewport header
def draw_lod_buttons(self, context):
    layout = self.layout
    scene = context.scene

    row = layout.row(align=True)

    # Collapse/Expand toggle button
    if scene.lod_buttons_expanded:
        op = row.operator("object.toggle_lod_buttons", text="> LODs Switches", emboss=True)
    else:
        op = row.operator("object.toggle_lod_buttons", text="< LODs Switches", emboss=True)

    # Show LOD buttons if expanded
    if scene.lod_buttons_expanded:
        
        # "Show All" button
        row.operator("object.show_all_lods",
                     text="All",
                     emboss=True,
                     icon="HIDE_OFF",
                     depress=(scene.active_lod == -1))
        
        # LOD0–LOD9
        for i in range(10):  
            op = row.operator("object.set_lod_header",
                              text=str(i),
                              emboss=True,
                              icon="OUTLINER_OB_MESH",
                              depress=(scene.active_lod == i))
            op.lod_value = i


classes = (
    OBJECT_OT_set_lod,
    OBJECT_OT_toggle_lod_buttons,
    OBJECT_OT_show_all_lods,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_HT_header.append(draw_lod_buttons)

    # Scene properties
    bpy.types.Scene.active_lod = bpy.props.IntProperty(default=-1)
    bpy.types.Scene.lod_buttons_expanded = bpy.props.BoolProperty(default=True)

def unregister():
    bpy.types.VIEW3D_HT_header.remove(draw_lod_buttons)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.active_lod
    del bpy.types.Scene.lod_buttons_expanded