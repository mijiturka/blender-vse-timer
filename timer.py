import bpy

bl_info = {
    "name": 'Animated Timer',
    "blender": (2, 93, 0),
    "category": "Sequencer",
}

addon_keymaps = []

class AnimatedTimer(bpy.types.Operator):
    '''Animated Timer'''
    bl_idname = 'sequencer.animated_timer'
    bl_label = 'Animated Timer'
    bl_options = {'REGISTER'}

    def execute(self, context):
        print('Executing AnimatedTimer')

        strip = context.scene.sequence_editor.active_strip
        print(strip)
        strip.text = "New text now!"

        strip_new = strip.copy()
        # for i in range(10):
#             scene.sequence_editor.link(strip_new)
#
#             strip_new.location = (obj.location * factor) + (cursor * (1.0 - factor))
#
#         bpy.ops.sequencer.duplicate_move(
#             SEQUENCER_OT_duplicate={"mode":'TRANSLATION'},
#             TRANSFORM_OT_seq_slide={"value":(0, 0), "snap":False,
# "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False,
# "snap_normal":(0, 0, 0), "release_confirm":False}
#         )

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(AnimatedTimer.bl_idname)

def register():
    bpy.utils.register_class(AnimatedTimer)

    bpy.types.SEQUENCER_MT_context_menu.append(menu_func)

    print("Registered AnimatedTimer")

def unregister():
    bpy.types.SEQUENCER_MT_context_menu.remove(menu_func)

    bpy.utils.unregister_class(AnimatedTimer)

    print("Unregistered AnimatedTimer")

if __name__ == '__main__':
    register()