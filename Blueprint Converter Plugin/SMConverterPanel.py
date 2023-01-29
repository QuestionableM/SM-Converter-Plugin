import bpy;

class BPCONV_PT_Panel(bpy.types.Panel):
    bl_idname = "BPCONV_PT_Panel";
    bl_label = "SM Converter Plugin";
    bl_category = "SM Converter Plugin";
    bl_space_type = "VIEW_3D";
    bl_region_type = "UI";

    def draw(self, context):
        layout = self.layout;
        
        layout.row().operator('view3d.smc_convert_assign_materials', text="Assign Materials");
        layout.row().operator('view3d.smc_convert_assign_materials_selected', text="Assign Materials Selected");
        layout.row().operator('view3d.smc_convert_create_nodes', text="Create Nodes");