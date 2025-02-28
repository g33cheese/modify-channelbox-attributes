# *********************************************************************
# content   = launches ui for modify channelbox attribute tool
# version   = 0.1.0
# date      = 2025-01-25
#
# how to    = draw_ui()
# to dos    = add reorder attribute buttons.
#
# author    = Garvey Chi (garveychi@gmail.com)
# *********************************************************************
'''Creates the UI for launching channelbox tools.'''

import importlib

import maya.cmds as cmds

import modify_channel_attrs as mod

importlib.reload(mod)


class Ui:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.sep_height = 20
        self.sep_style = 'none'

        # *********************************************************************
        # LAYOUT
        self.create_window(name, title)
        self.create_separator(self.sep_height, self.sep_style)

        cmds.rowLayout(numberOfColumns=2)

        cmds.setParent(self.layout)

        # *********************************************************************
        # BUTTONS
        self.create_button('Reset Channels',
                           lambda *args: mod.reset_channels(),
                           True, '-- RESET ATTRIBUTES --')
        self.create_button('Match Transforms',
                           lambda *args: mod.match_attribute('all'),
                           True, '-- MATCH ATTRIBUTES --')
        self.create_button('Match Translate',
                           lambda *args: mod.match_attribute('translate'))
        self.create_button('Match Rotate',
                           lambda *args: mod.match_attribute('rotate'))
        self.create_button('Match Scale',
                           lambda *args: mod.match_attribute('scale'))

        self.attribute_name = cmds.textFieldGrp(label='Attribute Name:',
                                                columnAlign=[1, 'left'],
                                                text='new_attr')
        self.attribute_type = cmds.optionMenuGrp(label='Attribute Type:',
                                                 columnAlign=[1, 'left'])
        self.enum_attr_name = cmds.textFieldGrp(label='Enum Names:',
                                                columnAlign=[1, 'left'],
                                                text='value1:value2:value3')
        self.min_max_attrs = cmds.floatFieldGrp(label='Min/Max:',
                                                numberOfFields=2,
                                                columnAlign=[1, 'left'])

        for attr_type in ['bool', 'int', 'float', 'enum']:
            self.create_menu_item(attr_type)

        self.create_button('Add Attribute',
                           lambda *args: mod.add_attribute(
                               self.attribute_name,
                               self.min_max_attrs,
                               self.enum_attr_name,
                               self.attribute_type),
                           True, '-- ADD/DEL ATTRIBUTES --')
        self.create_button('Add Separator',
                           lambda *args: mod.add_separator(
                               self.attribute_name))
        self.create_button('Delete Attribute',
                           lambda *args: mod.delete_attribute())
        self.create_button('Lock/Unlock Attribute',
                           lambda *args: mod.modify_attribute(
                               keyable=True, lock=True, channelBox=False),
                           True, '-- CHANNEL ATTRIBUTES --')
        self.create_button('Hide Attribute',
                           lambda *args: mod.modify_attribute(
                               keyable=False, lock=False, channelBox=False))
        self.create_button('Lock + Hide Attribute',
                           lambda *args: mod.modify_attribute(
                               keyable=False, lock=True, channelBox=False))
        self.create_button('Keyable/Unkeyable Attribute',
                           lambda *args: mod.modify_attribute(
                               keyable=False, lock=False, channelBox=True))
        self.create_button('Mute Attribute',
                           lambda *args: mod.mute_attribute())
        self.create_button('Unmute Attribute',
                           lambda *args: mod.mute_attribute(
                               disable=True, force=True))
        self.create_button('^', lambda *args: mod.reorder_attribute())
        self.create_button('v', lambda *args: mod.reorder_attribute())

        self.create_button('Connect Attributes',
                           lambda *args: mod.connect_attribute(),
                           True, '-- CONNECT ATTRIBUTES --')
        self.create_button('Disconnect Attributes',
                           lambda *args: mod.disconnect_attribute())

        # *********************************************************************
        # FORMATTING
        self.create_separator(40, self.sep_style)
        cmds.showWindow(self.window)

        # *********************************************************************
        # FUNC
    def create_window(self, name, title):
        if cmds.window(name, exists=True):
            cmds.deleteUI(name, window=True)
        self.window = cmds.window(name, title=title, sizeable=False, resizeToFitChildren=True)
        self.layout = cmds.rowColumnLayout(numberOfColumns=1, columnWidth=(1, 300))

    def create_separator(self, height_value, style_type):
        cmds.separator(height=height_value, style=style_type)

    def create_button(self, label_name, command, start=None, section=None):
        if start:
            self.create_separator(self.sep_height, 'singleDash')
            cmds.text(label=section, align='center')
            self.create_separator(self.sep_height, 'singleDash')
        cmds.button(label=label_name, command=command)

    def create_menu_item(self, attr_type):
        cmds.menuItem(label=attr_type)


ui_1 = Ui('channelboxToolWindow', 'ChannelBox Tools')
