# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Blueprint Converter Extension",
    "author" : "Questionable Mark",
    "description" : "",
    "blender" : (2, 92, 0),
    "version" : (0, 0, 7),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy;

from . AssignMaterials import AssignMaterials_Operator;
from . AssignMaterialsSelected import AssignMaterialsSelected_Operator;
from . CreateNodes import CreateNodes_Operator;
from . BlueprintConverterPanel import BPCONV_PT_Panel;

classes = (
    AssignMaterials_Operator,
    AssignMaterialsSelected_Operator,
    CreateNodes_Operator,
    BPCONV_PT_Panel
);

register, unregister = bpy.utils.register_classes_factory(classes);