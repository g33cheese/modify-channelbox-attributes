#*********************************************************************
# content	= Modify the channelbox. Reset attributes to default, 
# 			  add, lock, hide or connect attributes.
# version	= 0.1.0
# date		= 2025-01-31
# 
# author	= Garvey Chi
#*********************************************************************
''' A collection of small individual helper tools/functions that modify
the channelbox's attributes. 

The module is open-ended and additional tools can easily be added. 

The modify-channelbox-attrs tool's functions are accessed via its 
accompanying UI
'''

import maya.mel as mel
import maya.cmds as cmds

from functools import partial


#******************************************************************************
# QUERY
def check_for_selection():
	''' Check to see if a selection has been made. '''	
	sel_list = cmds.ls(selection=True)
	if not sel_list:
		cmds.warning('Nothing is selected.')

	return sel_list


def check_cbox_attributes():
	'''	Store the selected channels in a list. '''
	get_cbox_name = mel.eval('$temp = $gChannelBoxName')
	channel_list  = cmds.channelBox(get_cbox_name, query=True, selectedMainAttributes=True)

	return get_cbox_name, channel_list


def get_selected_channels():
	''' Returns channels that are selected in the channelbox. '''
	cbox_attr = check_cbox_attributes()[0]
	sel_main_attrs  = cmds.channelBox(cbox_attr, query=True, selectedMainAttributes=True)
	sel_shape_attrs = cmds.channelBox(cbox_attr, query=True, selectedShapeAttributes=True)
	sel_hist_attrs  = cmds.channelBox(cbox_attr, query=True, selectedHistoryAttributes=True)

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


#******************************************************************************
# CHANNELBOX TOOLS
def reset_channels():
	'''	Reset selected channels in the channel box to default,
	if nothing's selected resets all keyable channels to default.
	'''
	sel_list  = check_for_selection()
	chan_list = check_cbox_attributes()[1]
	for obj in sel_list:
		if not chan_list:
			chan_list = cmds.listAttr(obj, keyable=True, unlocked=True)
			
		for channel in chan_list:
			try:
				default_attribute = cmds.attributeQuery(channel, listDefault=True, node=obj)[0]
				cmds.setAttr('{0}.{1}'.format(obj, channel), default_attribute)
			except NameError:
				pass
	
	deselect_channels()


def match_attribute(attribute=None):
	sel_list = check_for_selection()
	if not sel_list:
		cmds.warning('Nothing is selected.')
	elif len(sel_list) == 1:
		cmds.warning('Only one object selected. Select another')
	else:
		tgt_node = sel_list[0]
		pos = cmds.xform(tgt_node, worldSpace=True, translation=True, query=True)
		rot = cmds.xform(tgt_node, worldSpace=True, rotation=True, query=True)
		sca = cmds.xform(tgt_node, worldSpace=True, scale=True, query=True)

	for match_node in sel_list[1:]:
		if attribute == 'translate':
				cmds.xform(match_node, worldSpace=True, translation=(pos[0], pos[1], pos[2]))
		elif attribute == 'rotate':
				cmds.xform(match_node, worldSpace=True, rotation=(rot[0], rot[1], rot[2]))
		elif attribute == 'scale':
				cmds.xform(match_node, worldSpace=True, scale=(sca[0], sca[1], sca[2]))
		elif attribute == 'all':
				cmds.xform(match_node, worldSpace=True,
						   translation=(pos[0], pos[1], pos[2]),
						   rotation=(rot[0], rot[1], rot[2]),
						   scale=(sca[0], sca[1], sca[2]))

	cmds.select(tgt_node, deselect=True)


def add_attribute(attribute_name):
	sel_list = check_for_selection()
	for obj in sel_list:
		attribute_name = cmds.textFieldGrp(attribute_name, query=True, text=True)
		full_name = '{0}.{1}'.format(obj, attribute_name)
		if cmds.objExists(full_name):
			cmds.warning('{0} already exists.'.format(full_name))
		else:
			cmds.addAttr(obj, longName=attribute_name, attributeType='bool')
			cmds.setAttr(full_name, keyable=True)


def add_separator(attribute_name):
	'''	Add a channelbox separator to selected object. '''
	sel_list = check_for_selection()
	for obj in sel_list:
		attribute_name = cmds.textFieldGrp(attribute_name, query=True, text=True)
		separator_name = '{0}'.format(attribute_name.upper())
		node_sep_name  = '{0}.{1}'.format(obj, separator_name)
		if not attribute_name:
			cmds.addAttr(obj, longName='___', attributeType='enum', enumName='---------------:')
			cmds.setAttr('{0}.___'.format(obj), keyable=True, lock=True)
		else:
			cmds.addAttr(obj, longName=separator_name, niceName='---{0}---'.format(
				separator_name), attributeType='enum', enumName='---------------:')
			cmds.setAttr(node_sep_name, keyable=True, lock=True)


def modify_attribute(**kwargs):
	sel_list  = check_for_selection()
	chan_list = check_cbox_attributes()[1]
	global last_modified
	for obj in sel_list:
		if not chan_list:
			chan_list = cmds.listAttr(obj, keyable=True, unlocked=True) # store keyable + unlocked attrs
			
			if chan_list:
				last_modified = [] # store the last modified attrs
				for chan in chan_list:
					full_name = '{0}.{1}'.format(obj, chan)
					if cmds.getAttr(full_name, **kwargs):
						cmds.setAttr(full_name, keyable=True, lock=False, channelBox=False) # Default
					else:
						cmds.setAttr(full_name, **kwargs)
					last_modified.append(chan)

			if not chan_list:
				for chan in last_modified:
					full_name = '{0}.{1}'.format(obj, chan)
					if cmds.getAttr(full_name, **kwargs):				
						cmds.setAttr(full_name, keyable=True, lock=False, channelBox=False) # Default
					else:
						cmds.setAttr(full_name, **kwargs)

		else: # modify or unmodify selected channels
			for chan in chan_list:
				full_name = '{0}.{1}'.format(obj, chan)
				if cmds.getAttr(full_name, **kwargs):
					cmds.setAttr(full_name, keyable=True, lock=False, channelBox=False) # Default
				else:
					cmds.setAttr(full_name, **kwargs)


def mute_attribute(**kwargs):
	sel_list  = check_for_selection()
	chan_list = check_cbox_attributes()[1]
	for obj in sel_list:
		if not chan_list:
			chan_list = cmds.listAttr(obj, keyable=True, unlocked=True)
			if chan_list:
				for chan in chan_list: 
					full_name = '{0}.{1}'.format(obj, chan)
					cmds.mute(full_name, **kwargs)

		else: 
			for chan in chan_list:
				full_name = '{0}.{1}'.format(obj, chan)
				cmds.mute(full_name, **kwargs)


def connect_attribute():
	sel_list = check_for_selection()
	chan_list = check_cbox_attributes()[1]
	if not sel_list:
		cmds.warning('Nothing is selected.')
	elif len(sel_list) == 1:
		cmds.warning('Only one object selected. Select another')
	else:
		for obj in sel_list:
			connect_attr_list = chan_list
			if not chan_list:
				connect_attr_list = cmds.listAttr(obj, keyable=True, unlocked=True)

		first_sel = sel_list[0]
		for next_sel in sel_list[1:]:
			for attr in connect_attr_list:
				cmds.connectAttr('{0}.{1}'.format(first_sel, attr), 
								 '{0}.{1}'.format(next_sel, attr), force=True)
		
		deselect_channels()

		cmds.select(deselect=True)


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
				plug = cmds.connectionInfo(destination_attr, getExactDestination=True)
				source = cmds.connectionInfo(plug, sourceFromDestination=True)
				cmds.disconnectAttr(source, plug)


def reorder_attribute():
	pass