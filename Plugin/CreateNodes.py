import bpy;
from . CreateNodeFunc import Add_SM_Nodes;

class CreateNodes_Operator(bpy.types.Operator):
    bl_idname = "view3d.bp_convert_create_nodes";
    bl_label = "Create SM Nodes";
    bl_description = "Adds all the useful nodes, to work with SM blueprints, if they don't exist yet";

    def execute(self, context):
        Add_SM_Nodes();

        return {'FINISHED'};