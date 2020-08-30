# Copyright 2020 Recep Aslantas.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

bl_info = {
    "name": "Asset Exchange format",
    "author": "Recep Aslantas",
    "version": (0, 1, 0),
    "blender": (2, 81, 6),
    "location": "File > Import-Export",
    "description": "Import-Export .ae File",
    "warning": "",
    "doc_url": "",
    "support": 'OFFICIAL',
    "category": "Import-Export",
}

if "bpy" in locals():
    import importlib
    if "import_ae" in locals():	
        importlib.reload(import_ae)
    if "export_ae" in locals():
        importlib.reload(export_ae)

class ExportAE(bpy.types.Operator, ExportGLTF2_Base, ExportHelper):
    """Export scene as Asset Exchange file"""

    bl_idname    = 'export_scene.ae'
    bl_label     = 'Export Asset Exchange'
    filename_ext = '.ae'

    filter_glob: StringProperty(default='*.ae', options={'HIDDEN'})


def menu_func_export(self, context):
    self.layout.operator(ExportAE.bl_idname, text='Asset Exchange (.ae)')
