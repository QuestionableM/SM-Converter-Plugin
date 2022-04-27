import bpy;

class BPCONV_PT_Panel(bpy.types.Panel):
    bl_idname = "BPCONV_PT_Panel";
    bl_label = "Blueprint Converter";
    bl_category = "Blueprint Converter";
    bl_space_type = "VIEW_3D";
    bl_region_type = "UI";

    def draw(self, context):
        layout = self.layout;
        
        layout.row().operator('view3d.bp_convert_assign_materials', text="Assign Materials");
        layout.row().operator('view3d.bp_convert_assign_materials_selected', text="Assign Materials Selected");
        layout.row().operator('view3d.bp_convert_create_nodes', text="Create Nodes");