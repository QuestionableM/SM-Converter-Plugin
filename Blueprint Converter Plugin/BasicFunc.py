from asyncio.windows_events import NULL
import bpy;

sm_known_materials = (
    "SM_DifAsgNor",
    "SM_Glass",
    "SM_Grass",
    "SM_Leaves",
    "SM_DifAsgNorAlpha",
    "SM_Water",
    "SM_LightCone",
    "SM_Liquid"
)

sm_material_table = {
    "1": {
        "name": "SM_DifAsgNor",
        "color_input_idx": 2
    },
    "2": {
        "name": "SM_Glass",
        "color_input_idx": 2
    },
    "3": {
        "name": "SM_Grass",
        "color_input_idx": 2
    },
    "4": {
        "name": "SM_Leaves",
        "color_input_idx": 2
    },
    "5": {
        "name": "SM_DifAsgNorAlpha",
        "color_input_idx": 2
    },
    "6": {
        "name": "SM_Water",
        "color_input_idx": 2
    },
    "7": {
        "name": "SM_LightCone",
        "color_input_idx": 2
    },
    "8": {
        "name": "SM_Liquid",
        "color_input_idx": 2
    }
}

def node_group_exists(name):
    node_groups = bpy.data.node_groups;
    node_amount = len(node_groups);

    for a in range(node_amount):
        cur_group = node_groups[a];

        if cur_group.name_full == name:
            return True;

    return False;

from uuid import UUID;

def is_color_valid(hex_string):
    try:
        int(hex_string, 16);
    except:
        return False;

    return True;

def is_uuid_valid(uuid_string):
    try:
        uuid_obj = UUID(uuid_string);
    except:
        return False;

    return str(uuid_obj) == uuid_string;

def is_mat_index_valid(material_index):
    mat_idx_str = material_index

    dot_idx = mat_idx_str.find(".")
    if dot_idx > -1:
        mat_idx_str = mat_idx_str[:dot_idx];

    if mat_idx_str[0] == "m":
        try:
            mat_idx_number = mat_idx_str[1:];
            int_test = int(mat_idx_number);

            if sm_material_table[mat_idx_number] == None:
                return False;

            return True;
        except:
            return False;

    return False;

def is_material_valid(mat_name):
    sep_name = mat_name.split(sep=" ");
    sep_name_len = len(sep_name);

    if sep_name_len < 3:
        return False;

    uuid_len = len(sep_name[0]);
    color_len = len(sep_name[1]);

    if uuid_len != 36 or color_len != 6:
        return False;

    if not is_uuid_valid(sep_name[0]) or not is_color_valid(sep_name[1]):
        return False;

    if sep_name_len == 4 and not is_mat_index_valid(sep_name[3]):
        return False;

    return True;


def check_if_has_node(nodes, name):
    node_amount = len(nodes);

    for a in range(node_amount):
        cur_node = nodes[a];

        if cur_node.name == name:
            return True;

    return False;

def remove_node_links(node_tree, node):
    for out in node.outputs:
        for lnk in out.links:
            node_tree.links.remove(lnk);

def srgb_to_linearrgb(c):
    if   c < 0:       return 0
    elif c < 0.04045: return c/12.92
    else:             return ((c+0.055)/1.055)**2.4

def hex_to_rgb(h, alpha=1):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple([srgb_to_linearrgb(c/0xff) for c in (r,g,b)] + [alpha])