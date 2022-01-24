import bpy;

sm_material_table = {
    "1": "SM_DifAsgNor",
    "2": "SM_Glass",
    "3": "SM_Grass",
    "4": "SM_Leaves",
    "5": "SM_DifAsgNorAlpha",
    "6": "SM_Water",
    "7": "SM_LightCone",
    "8": "SM_Liquid"
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
        uuid_obj = UUID(uuid_string, version=4);
    except:
        return False;

    return str(uuid_obj) == uuid_string;

def is_material_valid(mat_name):
    if len(mat_name) >= 43:
        mat_color = mat_name[37:43];

        return is_color_valid(mat_color);

    return False;


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