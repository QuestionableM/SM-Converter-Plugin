import bpy;
from . CreateNodeFunc import Add_SM_Nodes;
from . AssignMaterialsFunc import Assign_Materials_Func;

class AssignMaterials_Operator(bpy.types.Operator):
    bl_idname = "view3d.bp_convert_assign_materials";
    bl_label = "Assign Materials";
    bl_description = "Assigns materials automatically for SM blueprints";

    def execute(self, context):
        print("AssignMaterials_Operator");
        Add_SM_Nodes();

        Assign_Materials_Func(bpy.data.materials);

        return {'FINISHED'};