import bpy;
from . CreateNodeFunc import Add_SM_Nodes;
from . AssignMaterialsFunc import Assign_Materials_Func;

class AssignMaterialsSelected_Operator(bpy.types.Operator):
    bl_idname = "view3d.bp_convert_assign_materials_selected";
    bl_label = "Assign Materials Selected";
    bl_description = "Assigns the materials only to selected blueprints";

    def execute(self, context):
        Add_SM_Nodes();

        output_dict = {};

        for obj in bpy.context.selected_objects:
            mat_slots = obj.material_slots;

            for mat in mat_slots:
                output_dict[mat.name] = mat.material;

        Assign_Materials_Func(output_dict.values());

        return {'FINISHED'};