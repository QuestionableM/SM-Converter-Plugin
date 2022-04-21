import bpy;
from .BasicFunc import *;

def HasAnyOf(node_tree, obj_list):
    obj_count = len(obj_list);
    for i in range(obj_count):
        if check_if_has_node(node_tree, obj_list[i]):
            return True;

    return False;

def IsNodeValid(cur_mat):
    if not is_material_valid(cur_mat.name_full):
        return False;

    if cur_mat.node_tree == None:
        return False;

    if HasAnyOf(cur_mat.node_tree.nodes, sm_known_materials):
        return False;

    return True;

def FindNeededNodes(mat_nodes):
    dif_node = None;
    asg_node = None;
    nor_node = None;

    for cur_node in mat_nodes:
        if cur_node.bl_idname != "ShaderNodeTexImage":
            continue;

        node_links = cur_node.outputs[0];
        link_amount = len(node_links.links);
        for b in range(link_amount):
            cur_link = node_links.links[b];

            cur_link_socket = cur_link.to_socket.name;
            cur_link_node = cur_link.to_node.name;

            if cur_link_socket == 'Color' and cur_link_node == 'Normal Map':
                nor_node = cur_node;
                break;
            elif cur_link_socket == 'Base Color' and cur_link_node == 'Principled BSDF':
                dif_node = cur_node;
                break;
            elif cur_link_socket == 'Specular' and cur_link_node == 'Principled BSDF':
                asg_node = cur_node;
                break;

    return dif_node, asg_node, nor_node;

def GetMaterialOutputNode(mat_nodes):
    mat_output = None;

    for cur_node in mat_nodes:
        cnode_name = cur_node.bl_idname;

        if cnode_name == 'ShaderNodeOutputMaterial':
            if mat_output == None:
                mat_output = cur_node;
            continue;

        if cnode_name == 'ShaderNodeTexImage':
            continue;
        
        mat_nodes.remove(cur_node);

    return mat_output;

def CreateSMTexNode(mat_nodes, color, settings):
    node_name = settings["name"];

    sm_tex = mat_nodes.new('ShaderNodeGroup');
    sm_tex.node_tree = bpy.data.node_groups[node_name];
    sm_tex.location = (100, 300);
    sm_tex.name = node_name;

    sm_tex.inputs[settings["color_input_idx"]].default_value = hex_to_rgb(int(color, 16));

    return sm_tex;

def InitDifNode(dif, links, tex_shader):
    if dif != None:
        dif.location = (-300, 300);
        dif.hide = True;
        links.new(dif.outputs[0], tex_shader.inputs[0]);
        links.new(dif.outputs[1], tex_shader.inputs[1]);

def InitAsgNode(asg, links, tex_shader):
    if asg != None:
        asg.location = (-300, 250);
        asg.hide = True;
        links.new(asg.outputs[0], tex_shader.inputs[3]);
        links.new(asg.outputs[1], tex_shader.inputs[4]);

def InitNorNode(nor, links, tex_shader):
    if nor != None:
        nor.location = (-300, 200);
        nor.hide = True;
        links.new(nor.outputs[0], tex_shader.inputs[7]);

def ConnectWithOutputNode(out_node, links, tex_shader):
    if out_node != None:
        links.new(tex_shader.outputs[0], out_node.inputs[0]);

def Assign_Materials_Func(mat_array):
    for cur_mat in mat_array:
        if not IsNodeValid(cur_mat):
            continue;

        mat_sep_name = cur_mat.name_full.split(sep=" ");
        mat_sep_name_len = len(mat_sep_name);

        material_index = "1";

        if mat_sep_name_len == 4:
            material_index = mat_sep_name[3][1:];
            mat_dot_idx = material_index.find(".");

            if mat_dot_idx > -1:
                material_index = material_index[:mat_dot_idx];

        cur_node_data = sm_material_table[material_index];

        mat_nodes = cur_mat.node_tree.nodes;
        dif_node, asg_node, nor_node = FindNeededNodes(mat_nodes);
        material_output_node = GetMaterialOutputNode(mat_nodes);

        SM_Tex_Shader = CreateSMTexNode(mat_nodes, mat_sep_name[1], cur_node_data);

        node_links = cur_mat.node_tree.links;
        InitDifNode(dif_node, node_links, SM_Tex_Shader);
        InitAsgNode(asg_node, node_links, SM_Tex_Shader);
        InitNorNode(nor_node, node_links, SM_Tex_Shader);

        ConnectWithOutputNode(material_output_node, node_links, SM_Tex_Shader);