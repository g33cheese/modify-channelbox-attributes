from maya import cmds
from maya import mel


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