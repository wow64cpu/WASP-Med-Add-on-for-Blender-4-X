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

# -------------------------------- WASPmed ------------------------------------#
#-------------------------------- version 0.8 ---------------------------------#
#                                                                              #
#                                    WASP                                      #
#                                   (2020)                                     #
#                                                                              #
# http://http://www.wasproject.it/                                             #
#                                                                              #
################################################################################


# print("WASP Med Start!")


if "bpy" in locals():
    # print("WASP Med importlib start")
    import importlib
    importlib.reload(waspmed_scan)
    importlib.reload(waspmed_sculpt)
    importlib.reload(waspmed_generate)
    importlib.reload(waspmed_deform)
    importlib.reload(waspmed_crop)
    importlib.reload(waspmed_generate)
    importlib.reload(waspmed_print)
    # print("WASP Med importlib end")

else:
    # print("WASP Med import start")
    from . import waspmed_scan
    from . import waspmed_sculpt
    from . import waspmed_generate
    from . import waspmed_deform
    from . import waspmed_crop
    from . import waspmed_generate
    from . import waspmed_print
    # print("WASP Med import end")

import bpy, bmesh

bl_info = {
	"name": "Waspmed",
	"author": "WASP",
	"version": (0, 0, 8),
	"blender": (4, 2, 1),
	"location": "",
	"description": "Tools for medical devices",
	"warning": "",
	"wiki_url": ("https://github.com/wasproject/Blender-WASP-Med"),
	"tracker_url": "",
	"category": "Mesh"}

print("WASP Med bl_info", bl_info)

classes = (
    waspmed_scan.WASPMedObjectProp,
    waspmed_scan.WASPMedSceneProp,

    waspmed_scan.SCENE_OT_wm_setup,
    waspmed_scan.OBJECT_OT_wm_auto_origin,
    waspmed_scan.OBJECT_OT_wm_rebuild_mesh,
    waspmed_scan.MESH_OT_wm_cap_holes,
    waspmed_scan.OBJECT_OT_wm_add_measure_plane,
    waspmed_scan.OBJECT_OT_wm_measure_circumference,
    waspmed_scan.OBJECT_OT_wm_next,
    waspmed_scan.OBJECT_OT_wm_back,
    waspmed_scan.OBJECT_OT_wm_check_differences,
    waspmed_generate.OBJECT_OT_wm_weight_thickness,
    waspmed_generate.OBJECT_OT_wm_set_weight_paint,
    waspmed_generate.OBJECT_OT_wm_weight_add_subtract,
    waspmed_sculpt.OBJECT_OT_wm_set_sculpt,
    waspmed_sculpt.OBJECT_OT_wm_set_draw,
    waspmed_sculpt.OBJECT_OT_wm_set_smooth,
    waspmed_sculpt.OBJECT_OT_wm_set_grab,
    waspmed_crop.OBJECT_OT_wm_define_crop_planes,
    waspmed_crop.OBJECT_OT_wm_crop_geometry,
    waspmed_deform.OBJECT_OT_wm_add_lattice_to_object,
    waspmed_deform.OBJECT_OT_wm_edit_lattice,
    waspmed_deform.OBJECT_OT_wm_rotate_sections,

    waspmed_scan.WASPMED_PT_progress,
    waspmed_print.WASPMED_PT_print,
    waspmed_sculpt.WASPMED_PT_sculpt,
    waspmed_generate.WASPMED_PT_generate,
    waspmed_crop.WASPMED_PT_crop,
    waspmed_deform.WASPMED_PT_deform,
    waspmed_scan.WASPMED_PT_scan
)


def register():
    print("WASP Med register start")
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Object.waspmed_prop = bpy.props.PointerProperty(
        type=waspmed_scan.WASPMedObjectProp)
    bpy.types.Scene.waspmed_prop = bpy.props.PointerProperty(
        type=waspmed_scan.WASPMedSceneProp)
    print("WASP Med register end")

def unregister():
    print("WASP Med unregister start")
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    print("WASP Med unregister end")

if __name__ == "__main__":
    register()
