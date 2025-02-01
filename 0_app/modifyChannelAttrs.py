#*********************************************************************
# content	= Modify the channelbox. Reset attributes to default, add, lock, hide or connect attributes.
# version	= 0.1.0
# date		= 2025-01-31
# 
# author	= Garvey Chi
#*********************************************************************
import maya.mel as mel
import maya.cmds as cmds

from functools import partial



def check_for_selection():
	'''
	Check to see if a selection has been made
	'''
	
	sel_list = cmds.ls(selection=True)

	# If nothing is selected exit function
	if not sel_list:
		cmds.warning('Nothing is selected.')
	else:
		pass
	return sel_list


def check_cbox_attributes():
	'''
	Store the selected channels in a list
	'''

	# Get the channelBox attribute name
	get_cbox_name = mel.eval('$temp = $gChannelBoxName') 
	# Generate a channelBox attribute list
	channel_list = cmds.channelBox(get_cbox_name, query=True, selectedMainAttributes=True)

	return get_cbox_name, channel_list


def reset_channels():
	'''
	Reset selected channels in the channel box to default,
	if nothing's selected resets all keyable channels to default.
	'''
	
	sel_list = check_for_selection()
	chan_list = check_cbox_attributes()[1]

	#Set the selected objects' attributes to default
	for obj in sel_list:
		if not chan_list:
			chan_list = cmds.listAttr(obj, keyable=True, unlocked=True)        
		for channel in chan_list:
			try:
				#Find the attribute's default value
				default_attribute = cmds.attributeQuery(channel, listDefault=True, node=obj)[0]
				#Set the attribute back to default
				cmds.setAttr('{0}.{1}'.format(obj, channel), default_attribute)
			except NameError:
				pass
	
	deselect_channels()


def get_selected_channels():
	'''
	Returns channels that are selected in the channelbox.
	'''
	cbox_attr = check_cbox_attributes()[0]

	selected_main_attrs  = cmds.channelBox(cbox_attr, query=True, selectedMainAttributes=True)
	selected_shape_attrs = cmds.channelBox(cbox_attr, query=True, selectedShapeAttributes=True)
	selected_hist_attrs  = cmds.channelBox(cbox_attr, query=True, selectedHistoryAttributes=True)
	
	sel_ch_list = list()
	if selected_main_attrs:
		sel_ch_list.extend(selected_main_attrs)
	if selected_shape_attrs:
		sel_ch_list.extend(selected_shape_attrs)
	if selected_hist_attrs:
		sel_ch_list.extend(selected_hist_attrs)
		
	return sel_ch_list


def deselect_channels():
	'''
	Deselects selected channels in the channelBox by clearing selection and then re-selecting.
	'''

	sel_list = check_for_selection()

	if not get_selected_channels():
		return

	cmds.select(clear=True)
	cmds.evalDeferred(partial(cmds.select, sel_list))


def match_attribute(attribute='none'):
	'''
	Match the transforms (tr, rot, sc or all) of the first selected node then applies it to the subsequent selections.
	'''
	
	sel_list = check_for_selection()

	# If nothing is selected exit function
	if not sel_list:
		cmds.warning('Nothing is selected.')
	elif len(sel_list) == 1:
		cmds.warning('Only one object selected. Select another')
	else:
		tgt_node = sel_list[0]        
		pos = cmds.xform(tgt_node, worldSpace=True, translation=True, query=True)
		rot = cmds.xform(tgt_node, worldSpace=True, rotation=True, query=True)
		sca = cmds.xform(tgt_node, worldSpace=True, scale=True, query=True)

	if attribute == 'translate':
		for match_node in sel_list[1:]:
			cmds.xform(match_node, worldSpace=True, translation=(pos[0], pos[1], pos[2]))
			cmds.select(tgt_node, deselect=True)
	elif attribute == 'rotate':        
		for match_node in sel_list[1:]:
			cmds.xform(match_node, worldSpace=True, rotation=(rot[0], rot[1], rot[2]))
			cmds.select(tgt_node, deselect=True)
	elif attribute == 'scale':
		for match_node in sel_list[1:]:
			cmds.xform(match_node, worldSpace=True, scale=(sca[0], sca[1], sca[2]))
			cmds.select(tgt_node, deselect=True)
	elif attribute == 'all':
		for match_node in sel_list[1:]:
			cmds.xform(match_node, worldSpace=True,
					   translation=(pos[0], pos[1], pos[2]),
					   rotation=(rot[0], rot[1], rot[2]),
					   scale=(sca[0], sca[1], sca[2]))
			cmds.select(tgt_node, deselect=True)


def add_attribute(attribute_name):
	'''
	Add attribute to selected object.
	'''

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
	'''
	Add a channelbox separator to selected object.
	'''
	
	sel_list = check_for_selection()

	for obj in sel_list:
		attribute_name = cmds.textFieldGrp(attribute_name, query=True, text=True)
		separator_name = '{0}'.format(attribute_name.upper())
		node_sep_name = '{0}.{1}'.format(obj, separator_name)
		if not attribute_name:
			cmds.addAttr(obj, longName='___', attributeType='enum', enumName='---------------:')
			cmds.setAttr('{0}.___'.format(obj), keyable=True, lock=True)
		else:
			cmds.addAttr(obj, longName=separator_name, niceName='---{0}---'.format(separator_name), attributeType='enum', enumName='---------------:')
			cmds.setAttr(node_sep_name, keyable=True, lock=True)


def lock_unlock_attribute():
	'''
	Lock or unlock selected attributes
	'''

	sel_list  = check_for_selection()
	chan_list = check_cbox_attributes()[1]

	for obj in sel_list:	    
		if not channel_list:
			chan_list = cmds.listAttr(object, keyable=True, unlocked=True)
		else:
			pass

		for chan in chan_list:
			node_attr_name = '{0}.{1}'.format(obj, attrs)
			attr_status = cmds.getAttr(node_attr_name, lock=True)
			if attr_status == True:
				cmds.setAttr(node_attr_name, lock=False)
			else:
				cmds.setAttr(node_attr_name, lock=True)


def connect_attribute():
	'''
	Make a connection between attributes of selected objects.
	'''

	sel_list = check_for_selection()
	chan_list = check_cbox_attributes()[1]

	if not sel_list:
		cmds.warning('Nothing is selected.')
	elif len(sel_list) == 1:
		cmds.warning('Only one object selected. Select another')
	else:
		# Store the selected channels in a list
		# reset_channels.channel_list
		for obj in sel_list:
			connect_attr_list = chan_list
			# If no attributes selected than store all keyable and unlocked attributes
			if not chan_list:
				connect_attr_list = cmds.listAttr(obj, keyable=True, unlocked=True)
			else:
				pass
		first_sel = sel_list[0]

		for next_sel in sel_list[1:]:
			for attr in connect_attr_list:
				cmds.connectAttr('{0}.{1}'.format(first_sel, attr), '{0}.{1}'.format(next_sel, attr), force=True)
		
		deselect_channels()

		cmds.select(deselect=True)


def disconnect_attribute():
	'''
	Disconnect connected attributes
	'''
	
	sel_list = check_for_selection()
	chan_list = check_cbox_attributes()[1]

	for obj in sel_list:
		connect_attr_list = chan_list
		# If no attributes selected than store all keyable and unlocked attributes
		if not chan_list:
			connect_attr_list = cmds.listAttr(obj, keyable=True, unlocked=True)
			print('No attr selected')
			print(connect_attr_list)
		else:
			pass
			
		for attr in connect_attr_list:
			destination_attr = '{0}.{1}'.format(obj, attr)
			if cmds.connectionInfo(destination_attr, isDestination=True):
				plug = cmds.connectionInfo(destination_attr, getExactDestination=True)
				source = cmds.connectionInfo(plug, sourceFromDestination=True)
				cmds.disconnectAttr(source, plug)
			else:
				pass
