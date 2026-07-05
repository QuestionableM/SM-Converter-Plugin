import bpy
import os

import BasicFunc as bfunc

script_file = os.path.realpath(__file__)
plugin_directory = os.path.dirname(script_file)

SM_MATERIALS_BLEND_PATH = plugin_directory + "/SMMaterials.blend/NodeTree/"

def Add_SM_Nodes():
    for mat_id in bfunc.sm_material_table:
        mat_name = bfunc.sm_material_table[mat_id]["name"]

        if bfunc.node_group_exists(mat_name):
            continue

        print(mat_id, "->", mat_name)
        bpy.ops.wm.append(filename=mat_name, directory=SM_MATERIALS_BLEND_PATH)