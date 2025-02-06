import maya.mel as mel
import maya.cmds as cmds

from functools import partial


GET_CBOX_NAME = mel.eval('$temp = $gChannelBoxName') #Get the channelBox attribute name
SEL_LIST = cmds.ls(selection=True)


def check_for_selection():
	'''
	Check to see if a selection has been made
	'''
	
	# If nothing is selected exit function
	if not SEL_LIST:
		cmds.warning('Nothing is selected.')
	else:
		pass


def reset_channels():
	'''
	Reset selected channels in the channel box to default, 
	if nothing's selected resets all keyable channels to default.
	'''
	
	check_for_selection()

	#Store the selected channels in a list
	channel_list = cmds.channelBox(GET_CBOX_NAME, query=True, selectedMainAttributes=True)
	
	#Set the selected objects' attributes to default
	for object in checkSel.SEL_LIST:
		if not channel_list:
			channel_list = cmds.listAttr(object, keyable=True, unlocked=True)        
		for channel in channel_list:
			try:
				#Find the attribute's default value
				default_attribute = cmds.attributeQuery(channel, listDefault=True, node=object)[0]
				#Set the attribute back to default
				cmds.setAttr('{0}.{1}'.format(object, channel), default_attribute)
			except StandardError:
				pass
	
	deselect_channels()


def get_selected_channels():
	'''
	Returns channels that are selected in the channelbox.
	'''
	
	check_for_selection()
	
	selected_main_attrs  = cmds.channelBox(GET_CBOX_NAME, query=True, selectedMainAttributes=True)
	selected_shape_attrs = cmds.channelBox(GET_CBOX_NAME, query=True, selectedShapeAttributes=True)
	selected_hist_attrs  = cmds.channelBox(GET_CBOX_NAME, query=True, selectedHistoryAttributes=True)
	
	channel_list = list()
	if selected_main_attrs:
		channel_list.extend(selected_main_attrs)
	if selected_shape_attrs:
		channel_list.extend(selected_shape_attrs)
	if selected_hist_attrs:
		channel_list.extend(selected_hist_attrs)
		
	return channel_list


def deselect_channels():
	'''
	Deselects selected channels in the channelBox by clearing selection and then re-selecting.
	'''

	SEL_LIST
	if not get_selected_channels():
		return
	
	#De-select selection
	cmds.select(clear=True)
	cmds.evalDeferred(partial(cmds.select, checkSel.SEL_LIST))
