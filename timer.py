import bpy

bl_info = {
    "name": 'Turn Into Animated Timer',
    "blender": (2, 93, 0),
    "category": "Sequencer",
}

class AnimatedTimer(bpy.types.Operator):
    '''Turn Into Animated Timer'''
    bl_idname = 'sequencer.animated_timer'
    bl_label = 'Turn Into Animated Timer'
    bl_options = {'REGISTER'}

    def execute(self, context):
        print('Executing AnimatedTimer')

        strip = context.scene.sequence_editor.active_strip

        timer_start = strip.frame_start
        timer_end = strip.frame_final_end

        # Split the strip into 1-frame strips

        ## Use the original as the first one
        timer_value = 0
        strip.frame_final_end = strip.frame_start + 1

        ## Create more strips, up until the end of the original
        current_position = strip.frame_final_end
        while current_position < timer_end:
            bpy.ops.sequencer.duplicate()
            current_strip = context.scene.sequence_editor.active_strip
            current_strip.frame_start = current_position
            current_strip.frame_final_end = current_position + 1

            current_strip.text = str(timer_value)

            timer_value += 1
            current_position += 1

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
