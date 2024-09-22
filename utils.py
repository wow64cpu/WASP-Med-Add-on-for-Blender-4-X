# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import bpy

def simple_to_mesh(ob):
    hide = False
    if ob.hide_viewport:
        hide = True
        ob.hide_viewport = False
    dg = bpy.context.evaluated_depsgraph_get()
    ob_eval = ob.evaluated_get(dg)
    me = bpy.data.meshes.new_from_object(ob_eval, preserve_all_data_layers=True, depsgraph=dg)
    # me.calc_normals()
    # me.flip_normals()
    ob.hide_viewport = hide
    return me


def setup_plane_with_constraints(context, name, constraint_type, bound_box, parent):
    """
    Creates a plane, sets up a constraint, and links it to the parent object.
    Args:
        :param context:
        :param name: The name of the plane being created.
        :param constraint_type: Constraint type ('min_x', 'max_x', 'min_z', 'max_z').
        :param bound_box: The bounding box object.
        :param parent: Parent object for the plane.
    """

    plane = context.object
    plane.name = name
    plane.constraints.new(type='LIMIT_LOCATION')

    match constraint_type:
        case 'min_x':
            plane.constraints[0].use_min_x = True
            plane.constraints[0].min_x = bound_box.x
            plane.dimensions = parent.dimensions.zyx
        case 'max_x':
            plane.constraints[0].use_max_x = True
            plane.constraints[0].max_x = bound_box.x
            plane.dimensions = parent.dimensions.zyx
        case 'min_z':
            plane.constraints[0].use_min_z = True
            plane.constraints[0].min_z = bound_box.z
            plane.dimensions = parent.dimensions.xyz
        case 'max_z':
            plane.constraints[0].use_max_z = True
            plane.constraints[0].max_z = bound_box.z
            plane.dimensions = parent.dimensions.xyz

    plane.hide_select = True
    plane.parent = parent


def draw_object_mode_panel(col, context):
    if context.mode is 'OBJECT':
        col.separator()
        col.operator("object.wm_add_measure_plane", text="Add Measure Plane", icon='MESH_CIRCLE')
        col.operator("object.wm_measure_circumference", text="Measure Circumferences", icon='DRIVER_DISTANCE')

    col.separator()

    col.operator("screen.region_quadview", text="Toggle Quad View", icon='VIEW3D')

    col.separator()

    row = col.row(align=True)
    row.operator("ed.undo", icon='LOOP_BACK')
    row.operator("ed.redo", icon='LOOP_FORWARDS')


def draw_measurement_tools_panel(layout, context):
    box = layout.box()
    col = box.column(align=True)

    if context.mode == 'PAINT_WEIGHT':
        col.operator("object.wm_check_differences",
                     icon="ZOOM_SELECTED",
                     text="Check Differences Off")
    else:
        col.operator("object.wm_check_differences",
                     icon="ZOOM_SELECTED",
                     text="Check Differences On")

    draw_object_mode_panel(col, context)
