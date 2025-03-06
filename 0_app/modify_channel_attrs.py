# *********************************************************************
# content  = Modify the channelbox. Reset attributes to default,
#            add, lock, hide or connect attributes.
# version  = 0.1.2
# date     = 2025-01-31
#
# author   = Garvey Chi
# *********************************************************************
''' A collection of small individual helper tools/functions that modify
the channelbox's attributes.
The module is open-ended and additional tools can easily be added.
The modify-channelbox-attrs tool's functions are accessed via its
accompanying UI
'''

import maya.mel as mel
import maya.cmds as cmds

from functools import partial


# ******************************************************************************
# QUERY
def check_for_selection():
    ''' Check to see if a selection has been made. '''
    sel_list = cmds.ls(selection=True)
    if not sel_list:
        cmds.warning('Nothing is selected.')

    return sel_list


def check_cbox_attributes():
    ''' Store the selected channels in a list. '''
    get_cbox_name = mel.eval('$temp = $gChannelBoxName')
    channel_list = cmds.channelBox(get_cbox_name,
                                   query=True,
                                   selectedMainAttributes=True)

    return get_cbox_name, channel_list


def get_selected_channels():
    ''' Returns channels that are selected in the channelbox. '''
    cbox_attr = check_cbox_attributes()[0]
    sel_main_attrs = cmds.channelBox(cbox_attr,
                                     query=True,
                                     selectedMainAttributes=True)
    sel_shape_attrs = cmds.channelBox(cbox_attr,
                                      query=True,
                                      selectedShapeAttributes=True)
    sel_hist_attrs = cmds.channelBox(cbox_attr,
                                     query=True,
                                     selectedHistoryAttributes=True)

    sel_ch_list = []
    if sel_main_attrs:
        sel_ch_list.extend(sel_main_attrs)
    if sel_shape_attrs:
        sel_ch_list.extend(sel_shape_attrs)
    if sel_hist_attrs:
        sel_ch_list.extend(sel_hist_attrs)

    return sel_ch_list


def deselect_channels():
    sel_list = check_for_selection()
    if not get_selected_channels():
        return
    cmds.select(clear=True)
    cmds.evalDeferred(partial(cmds.select, sel_list))


# ******************************************************************************
# CHANNELBOX TOOLS
def reset_channels():
    ''' Reset selected channels in the channel box to default,
    if nothing's selected resets all keyable channels to default.
    '''
    sel_list = check_for_selection()
    chan_list = check_cbox_attributes()[1]
    for obj in sel_list:
        if not chan_list:
            chan_list = cmds.listAttr(obj, keyable=True, unlocked=True)

        for channel in chan_list:
            default_attribute = cmds.attributeQuery(
                channel, listDefault=True, node=obj)[0]
            cmds.setAttr('{0}.{1}'.format(obj, channel), default_attribute)

    deselect_channels()


def match_attribute(attribute):
    sel_list = check_for_selection()
    tgt_node = None
    if sel_list:
        tgt_node = sel_list[0]
        pos = cmds.xform(tgt_node, worldSpace=True, translation=True, query=True)
        rot = cmds.xform(tgt_node, worldSpace=True, rotation=True, query=True)
        sca = cmds.xform(tgt_node, worldSpace=True, scale=True, query=True)
    if len(sel_list) == 1:
        cmds.warning('Only one object selected. Select another')
    elif not sel_list:
        cmds.warning('Nothing is selected.')
    for match_node in sel_list[1:]:
        if attribute == 'translate':
            cmds.xform(match_node,
                       worldSpace=True,
                       translation=(pos[0], pos[1], pos[2]))
        elif attribute == 'rotate':
            cmds.xform(match_node,
                       worldSpace=True,
                       rotation=(rot[0], rot[1], rot[2]))
        elif attribute == 'scale':
            cmds.xform(match_node,
                       worldSpace=True,
                       scale=(sca[0], sca[1], sca[2]))
        elif attribute == 'all':
            cmds.xform(match_node,
                       worldSpace=True,
                       translation=(pos[0], pos[1], pos[2]),
                       rotation=(rot[0], rot[1], rot[2]),
                       scale=(sca[0], sca[1], sca[2]))
        cmds.select(tgt_node, deselect=True)


def add_attribute(attr_name, min_value, max_value, enum_name, attr_type=None):
    sel_list = check_for_selection()

    for obj in sel_list:
        full_name = '{0}.{1}'.format(obj, attr_name)
        if cmds.objExists(full_name):
            cmds.warning('{0} already exists.'.format(full_name))
        elif attr_type == 'int':
            cmds.addAttr(obj,
                         longName=attr_name,
                         attributeType='long',
                         min=min_value,
                         max=max_value)
        elif attr_type == 'enum':
            cmds.addAttr(obj,
                         longName=attr_name,
                         attributeType='enum',
                         enumName=enum_name)
        else:
            cmds.addAttr(obj,
                         longName=attr_name,
                         attributeType=attr_type,
                         min=min_value,
                         max=max_value)
        cmds.setAttr(full_name, keyable=True)


def add_separator(attr_name):
    ''' Add a channelbox separator to selected object. '''
    sel_list = check_for_selection()
    # attr_name = cmds.textFieldGrp(attr_name, query=True, text=True)
    separator_name = '{0}'.format(attr_name.upper())
    sep_def_name = '___'
    sep_enum_name = '---------------:'

    for obj in sel_list:
        full_name = '{0}.{1}'.format(obj, separator_name)
        if attr_name and not cmds.objExists(full_name):
            cmds.addAttr(obj,
                         longName=separator_name,
                         niceName='---{0}---'.format(separator_name),
                         attributeType='enum',
                         enumName=sep_enum_name)
            cmds.setAttr('{0}.{1}'.format(obj, separator_name),
                         keyable=True, lock=True)
        elif attr_name and cmds.objExists(full_name):
            custom_attrs = cmds.listAttr(obj, keyable=True, userDefined=True)
            sep_attr_name = '{0}{1}'.format('_', custom_attrs[-1])
            cmds.addAttr(obj,
                         longName=sep_attr_name,
                         niceName='{0}{1}'.format('_', custom_attrs[-1]),
                         attributeType='enum',
                         enumName=sep_enum_name)
            cmds.setAttr('{0}.{1}'.format(obj, sep_attr_name),
                         keyable=True, lock=True)
        elif not attr_name:  # generic separator attribute:
            try:
                cmds.addAttr(obj,
                             longName=sep_def_name,
                             attributeType='enum',
                             enumName=sep_enum_name)
                cmds.setAttr('{0}.{1}'.format(obj, sep_def_name),
                             keyable=True, lock=True)
            except Exception:
                custom_attrs = cmds.listAttr(obj,
                                             keyable=True,
                                             userDefined=True)
                ext_sep_name = '{0}{1}'.format(custom_attrs[-1], '_')
                cmds.addAttr(obj,
                             longName=ext_sep_name,
                             attributeType='enum',
                             enumName=sep_enum_name)
                cmds.setAttr('{0}.{1}'.format(obj, ext_sep_name),
                             keyable=True, lock=True)


def delete_attribute():
    sel_list = check_for_selection()
    chan_list = check_cbox_attributes()[1]
    for obj in sel_list:
        if chan_list:
            for chan in chan_list:
                full_name = '{0}.{1}'.format(obj, chan)
                if cmds.objExists(full_name):
                    cmds.setAttr(full_name, lock=False)
                    cmds.deleteAttr(full_name)
                else:
                    break


def modify_attribute(**kwargs):
    global last_modified
    sel_list = check_for_selection()
    chan_list = check_cbox_attributes()[1]
    for obj in sel_list:
        if chan_list:  # modify or unmodify selected channels
            for chan in chan_list:
                full_name = '{0}.{1}'.format(obj, chan)
                if cmds.getAttr(full_name, **kwargs):
                    cmds.setAttr(full_name,
                                 keyable=True,
                                 lock=False,
                                 channelBox=False)  # Default
                else:
                    cmds.setAttr(full_name, **kwargs)
        if not chan_list:
            # store keyable  unlocked attrs
            chan_list = cmds.listAttr(obj, keyable=True, unlocked=True)
            if chan_list:
                last_modified = []  # store the last modified attrs
                for chan in chan_list:
                    full_name = '{0}.{1}'.format(obj, chan)
                    if cmds.getAttr(full_name, **kwargs):
                        cmds.setAttr(full_name,
                                     keyable=True,
                                     lock=False,
                                     channelBox=False)  # Default
                    else:
                        cmds.setAttr(full_name, **kwargs)
                    last_modified.append(chan)
            else:
                for chan in last_modified:
                    full_name = '{0}.{1}'.format(obj, chan)
                    if cmds.getAttr(full_name, **kwargs):
                        cmds.setAttr(full_name,
                                     keyable=True,
                                     lock=False,
                                     channelBox=False)  # Default
                    else:
                        cmds.setAttr(full_name, **kwargs)


def mute_attribute(**kwargs):
    sel_list = check_for_selection()
    chan_list = check_cbox_attributes()[1]
    for obj in sel_list:
        if chan_list:
            for chan in chan_list:
                full_name = '{0}.{1}'.format(obj, chan)
                cmds.mute(full_name, **kwargs)
        else:
            chan_list = cmds.listAttr(obj, keyable=True, unlocked=True)
            if chan_list:
                for chan in chan_list:
                    full_name = '{0}.{1}'.format(obj, chan)
                    cmds.mute(full_name, **kwargs)


def connect_attribute():
    sel_list = check_for_selection()
    chan_list = check_cbox_attributes()[1]
    if len(sel_list) == 1:
        cmds.warning('Only one object selected. Select another')
    elif not sel_list:
        cmds.warning('Nothing is selected.')
    else:
        for obj in sel_list:
            connect_attr_list = chan_list
            if not chan_list:
                connect_attr_list = cmds.listAttr(
                    obj, keyable=True, unlocked=True)

        first_sel = sel_list[0]
        for next_sel in sel_list[1:]:
            for attr in connect_attr_list:
                cmds.connectAttr('{0}.{1}'.format(first_sel, attr),
                                 '{0}.{1}'.format(next_sel, attr), force=True)
        deselect_channels()

        # cmds.select(deselect=True)


def disconnect_attribute():
    sel_list = check_for_selection()
    chan_list = check_cbox_attributes()[1]
    for obj in sel_list:
        connect_attr_list = chan_list
        if not chan_list:
            connect_attr_list = cmds.listAttr(obj, keyable=True, unlocked=True)

        for attr in connect_attr_list:
            destination_attr = '{0}.{1}'.format(obj, attr)
            if cmds.connectionInfo(destination_attr, isDestination=True):
                plug = cmds.connectionInfo(
                    destination_attr, getExactDestination=True)
                src = cmds.connectionInfo(plug, sourceFromDestination=True)
                cmds.disconnectAttr(src, plug)


def reorder_attribute():
    pass
