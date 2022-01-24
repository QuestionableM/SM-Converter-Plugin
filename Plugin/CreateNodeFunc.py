import bpy;
from . BasicFunc import node_group_exists, sm_material_table

def Add_SM_Nodes():
    for mat_id in sm_material_table:
        mat_name = sm_material_table[mat_id];

        if node_group_exists(mat_name):
            continue;

        print(mat_id, "->", sm_material_table[mat_id]);
        bpy.ops.wm.append(filename=mat_name, directory=".\\SMMaterials.blend\\NodeTree\\")