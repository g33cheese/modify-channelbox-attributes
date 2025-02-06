import maya.mel as mel
import maya.cmds as cmds

from functools import partial

def resetChannels():
    '''Resets selected channels in the channel box to default, or if nothing's selected, resets all keyable channels to default.'''
    
    #Get the channelBox attribute name
    get_channelbox_name = mel.eval('$temp = $gChannelBoxName')
    
    selection_list = cmds.ls(selection=True)
    
    #If nothing is selected exit the module
    if not selection_list:
        return
    
    #Store the selected channels in a list
    channel_list = cmds.channelBox(get_channelbox_name, query=True, selectedMainAttributes=True)
    
    #Set the selected objects' attributes to default
    for object in selection_list:
        attribute_list = channel_list
        if not channel_list:
            attribute_list = cmds.listAttr(object, keyable=True, unlocked=True)
        
        for attribute in attribute_list:
            try:
                #Find the attribute's default value
                default_attribute = cmds.attributeQuery(attribute, listDefault=True, node=object)[0]
                #Set the attribute back to default
                cmds.setAttr('{0}.{1}'.format(object, attribute), default_attribute)
            except StandardError:
                pass
    
    deselectChannels()


def getSelectedChannels():
    '''Module returns channels that are selected in the channelbox.'''
    
    #Query whether or not channels are selected 
    if not cmds.ls(selection=True):
        return
    
    #Get the channelBox attribute name    
    get_channelbox_name = mel.eval('$temp = $gChannelBoxName')
    
    selected_main_attrs = cmds.channelBox(get_channelbox_name, query=True, selectedMainAttributes=True)
    selected_shape_attrs = cmds.channelBox(get_channelbox_name, query=True, selectedShapeAttributes=True)
    selected_history_attrs = cmds.channelBox(get_channelbox_name, query=True, selectedHistoryAttributes=True)
    
    channel_list = list()
    if selected_main_attrs:
        channel_list.extend(selected_main_attrs)
    if selected_shape_attrs:
        channel_list.extend(selected_shape_attrs)
    if selected_history_attrs:
        channel_list.extend(selected_history_attrs)
        
    return channel_list


def deselectChannels():
    '''Module deselects selected channels in the channelBox by clearing selection and then re-selecting.'''
    
    if not getSelectedChannels():
        return
    
    selected = cmds.ls(selection=True)
    
    #De-select selection
    cmds.select(clear=True)
    cmds.evalDeferred(partial(cmds.select, selected))

