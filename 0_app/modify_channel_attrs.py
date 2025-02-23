# *********************************************************************
# content   = Modify the channelbox. Reset attributes to default,
#             add, lock, hide or connect attributes.
# version   = 0.1.0
# date      = 2025-01-31
#
# author    = Garvey Chi
# *********************************************************************
''' A collection of small individual helper tools/functions that modify
the channelbox's attributes.

The module is open-ended and additional tools can easily be added.

The modify-channelbox-attrs tool's functions are accessed via its
accompanying UI
'''

import json
import maya.mel as mel
import maya.cmds as cmds

from functools import partial


class ChannelBoxTools(object):
    '''
    Added a class to utilize easier sharing of variables between functions.
    Class allowed removal of many duplicate variables.
    Removed check_cbox_attributes func, not needed once the class was added.
    '''

    def __init__(self):
        self.sel_list = cmds.ls(selection=True)
        self.cbox_attr = self.cbox_attributes()[0]
        self.get_cbox_name = mel.eval('$temp = $gChannelBoxName')
        self.channel_list = cmds.channelBox(self.get_cbox_name, query=True,
                                            selectedMainAttributes=True)
        self.tgt_node = self.sel_list[0]

    # ******************************************************************************
    # QUERY

    # Decorator
    def decorator(func):
        def wrapper():
            print('Start')
            func()
            print('Complete')
        return wrapper

    def check_for_selection(self):
        '''Check to see if a selection has been made.'''
        if not self.sel_list:
            cmds.warning('Nothing is selected.')

        return self.sel_list

    @decorator
    def get_selected_channels(self):
        ''' Returns channels that are selected in the channelbox. '''
        sel_main_attrs = cmds.channelBox(self.cbox_attr, query=True,
                                         selectedMainAttributes=True)
        sel_shape_attrs = cmds.channelBox(self.cbox_attr, query=True,
                                          selectedShapeAttributes=True)
        sel_hist_attrs = cmds.channelBox(self.cbox_attr, query=True,
                                         selectedHistoryAttributes=True)
        sel_ch_list = []
        if sel_main_attrs:
            sel_ch_list.extend(sel_main_attrs)
        if sel_shape_attrs:
            sel_ch_list.extend(sel_shape_attrs)
        if sel_hist_attrs:
            sel_ch_list.extend(sel_hist_attrs)

        return sel_ch_list

    def deselect_channels(self):
        if not self.get_selected_channels():
            return
        cmds.select(clear=True)
        cmds.evalDeferred(partial(cmds.select, self.sel_list))

    # ******************************************************************************
    # CHANNELBOX TOOLS
    def reset_channels(self):
        ''' Reset selected channels in the channel box to default,
        if nothing's selected resets all keyable channels to default.
        '''
        for obj in self.sel_list:
            if not self.channel_list:
                self.channel_list = cmds.listAttr(
                    obj, keyable=True, unlocked=True)

            for channel in self.channel_list:
                try:
                    default_attribute = cmds.attributeQuery(
                        channel, listDefault=True, node=obj)[0]
                    cmds.setAttr('{0}.{1}'.format(obj, channel),
                                 default_attribute)
                except NameError:
                    pass

        self.deselect_channels()

    def match_attribute(self, attribute):
        if self.sel_list:
            pos = cmds.xform(self.tgt_node, worldSpace=True, translation=True,
                             query=True)
            rot = cmds.xform(self.tgt_node, worldSpace=True, rotation=True,
                             query=True)
            sca = cmds.xform(self.tgt_node, worldSpace=True, scale=True,
                             query=True)
        elif len(self.sel_list) == 1:
            cmds.warning('Only one object selected. Select another')
        else:
            cmds.warning('Nothing is selected.')

        for match_node in self.sel_list[1:]:
            if attribute == 'translate':
                cmds.xform(match_node, worldSpace=True,
                           translation=(pos[0], pos[1], pos[2]))
            elif attribute == 'rotate':
                cmds.xform(match_node, worldSpace=True,
                           rotation=(rot[0], rot[1], rot[2]))
            elif attribute == 'scale':
                cmds.xform(match_node, worldSpace=True,
                           scale=(sca[0], sca[1], sca[2]))
            elif attribute == 'all':
                cmds.xform(match_node, worldSpace=True,
                           translation=(pos[0], pos[1], pos[2]),
                           rotation=(rot[0], rot[1], rot[2]),
                           scale=(sca[0], sca[1], sca[2]))

        cmds.select(self.tgt_node, deselect=True)

    def add_attribute(self, attribute_name, min_max, en_attr_name,
                      attribute_type=None):
        self.attr_name = cmds.textFieldGrp(attribute_name, query=True, text=True)
        self.enum_name = cmds.textFieldGrp(en_attr_name, query=True, text=True)
        self.min_value = cmds.floatFieldGrp(min_max, query=True, value1=True)
        self.max_value = cmds.floatFieldGrp(min_max, query=True, value2=True)
        self.attr_type = cmds.optionMenuGrp(attribute_type, query=True, value=True)

        for obj in self.sel_list:
            full_name = '{0}.{1}'.format(obj, self.attr_name)
            if cmds.objExists(full_name):
                cmds.warning('{0} already exists.'.format(full_name))
            elif self.attr_type == 'int':
                cmds.addAttr(obj, longName=self.attr_name,
                             attributeType='long',
                             min=self.min_value, max=self.max_value)
            elif self.attr_type == 'enum':
                cmds.addAttr(obj, longName=self.attr_name,
                             attributeType='enum', enumName=self.enum_name)
            else:
                cmds.addAttr(obj, longName=self.attr_name,
                             attributeType=self.attr_type,
                             min=self.min_value, max=self.max_value)
            cmds.setAttr(full_name, keyable=True)

    def add_separator(self, attribute_name):
        ''' Add a channelbox separator to selected object. '''
        separator_name = '{0}'.format(attribute_name.upper())
        sep_def_name = '___'
        sep_enum_name = '---------------:'

        for obj in self.sel_list:
            if self.attr_name and not cmds.objExists('{0}.{1}'.format(
                                                     obj, separator_name)):
                cmds.addAttr(obj, longName=separator_name,
                             niceName='---{0}---'.format(separator_name),
                             attributeType='enum', enumName=sep_enum_name)
                cmds.setAttr('{0}.{1}'.format(obj, separator_name),
                             keyable=True, lock=True)
            elif self.attr_name and cmds.objExists(
                    '{0}.{1}'.format(obj, separator_name)):
                custom_attrs = cmds.listAttr(obj, keyable=True,
                                             userDefined=True)
                sep_attr_name = '{0}{1}'.format('_', custom_attrs[-1])
                cmds.addAttr(obj, longName=sep_attr_name,
                             niceName='{0}{1}'.format('_', custom_attrs[-1]),
                             attributeType='enum', enumName=sep_enum_name)
                cmds.setAttr('{0}.{1}'.format(obj, sep_attr_name),
                             keyable=True, lock=True)
            elif not self.attr_name:  # generic separator attribute:
                try:
                    cmds.addAttr(obj, longName=sep_def_name,
                                 attributeType='enum', enumName=sep_enum_name)
                    cmds.setAttr('{0}.{1}'.format(obj, sep_def_name),
                                 keyable=True, lock=True)
                except Exception:
                    custom_attrs = cmds.listAttr(obj, keyable=True,
                                                 userDefined=True)
                    ext_sep_name = '{0}{1}'.format(custom_attrs[-1], '_')
                    cmds.addAttr(obj, longName=ext_sep_name,
                                 attributeType='enum', enumName=sep_enum_name)
                    cmds.setAttr('{0}.{1}'.format(obj, ext_sep_name),
                                 keyable=True, lock=True)

    def delete_attribute(self):
        for obj in self.sel_list:
            if self.channel_list:
                for chan in self.channel_list:
                    self.complete_name = '{0}.{1}'.format(obj, chan)
                    if cmds.objExists(self.complete_name):
                        cmds.setAttr(self.complete_name, lock=False)
                        cmds.deleteAttr(self.complete_name)
                    else:
                        break


    def modify_attribute(self, **kwargs):
        for obj in self.sel_list:
            if self.channel_list:  # modify or unmodify selected channels
                for chan in self.channel_list:
                    if cmds.getAttr(self.complete_name, **kwargs):
                        cmds.setAttr(self.complete_name, keyable=True,
                                     lock=False, channelBox=False)  # Default
                    else:
                        cmds.setAttr(self.complete_name, **kwargs)
            if not self.channel_list:
                # store keyable + unlocked attrs
                self.channel_list = cmds.listAttr(obj, keyable=True,
                                                  unlocked=True)
                if self.channel_list:
                    self.last_modified = []  # store the last modified attrs
                    for chan in self.channel_list:
                        if cmds.getAttr(self.complete_name, **kwargs):
                            cmds.setAttr(self.complete_name, keyable=True,
                                         lock=False, channelBox=False)
                        else:
                            cmds.setAttr(self.complete_name, **kwargs)
                        self.last_modified.append(chan)
                else:
                    for chan in self.last_modified:
                        if cmds.getAttr(self.complete_name, **kwargs):
                            cmds.setAttr(self.complete_name, keyable=True,
                                         lock=False, channelBox=False)
                        else:
                            cmds.setAttr(self.complete_name, **kwargs)

    def mute_attribute(self, **kwargs):
        for obj in self.sel_list:
            if self.channel_list:
                for chan in self.channel_list:
                    cmds.mute(self.complete_name, **kwargs)
            else:
                self.channel_list = cmds.listAttr(obj, keyable=True,
                                                  unlocked=True)
                if self.channel_list:
                    for chan in self.channel_list:
                        cmds.mute(self.complete_name, **kwargs)

    def connect_attribute(self):
        if len(self.sel_list) == 1:
            cmds.warning('Only one object selected. Select another')
        elif not self.sel_list:
            cmds.warning('Nothing is selected.')
        else:
            for obj in self.sel_list:
                connect_attr_list = self.channel_list
                if not self.channel_list:
                    connect_attr_list = cmds.listAttr(obj, keyable=True,
                                                      unlocked=True)
            self.first_sel = self.sel_list[0]
            for next_sel in self.sel_list[1:]:
                for attr in connect_attr_list:
                    cmds.connectAttr('{0}.{1}'.format(self.first_sel, attr),
                                     '{0}.{1}'.format(next_sel, attr),
                                     force=True)
            self.deselect_channels()

            cmds.select(deselect=True)

    def disconnect_attribute(self):
        for obj in self.sel_list:
            connect_attr_list = self.channel_list
            if not self.channel_list:
                connect_attr_list = cmds.listAttr(obj, keyable=True,
                                                  unlocked=True)

            for attr in connect_attr_list:
                destination_attr = '{0}.{1}'.format(obj, attr)
                if cmds.connectionInfo(destination_attr, isDestination=True):
                    plug = cmds.connectionInfo(
                        destination_attr, getExactDestination=True)
                    src = cmds.connectionInfo(plug, sourceFromDestination=True)
                    cmds.disconnectAttr(src, plug)

    def export_attribute(self):
        '''
        Why would a data file would improve this module?
        For this App a config or data file doesn't really fit its purpose.
        However, for another rig-specific app I would use data files to write
            out joint or control data. Or attribute data to save a pose, etc.
        '''
        self.obj_values = {}

        json_path = r'D:\python\python_advanced\0_app\data\{0}_values.json'.format(self.first_sel)
        user_data = self.obj_values

        with open(json_path, 'w') as file:
            json.dump(user_data, file, indent=4)

        for sel in self.sel_list:
            if not self.channel_list:
                self.channel_list = cmds.listAttr(sel, keyable=True, unlocked=True)
            for attr in self.channel_list:
                attr_value = cmds.getAttr(self.complete_name)
                self.obj_values[self.complete_name] = attr_value

        print('Writing attribute values to json...')
