#*********************************************************************
# content	= description
# version	= 1.0.0
# date		= year-month-day
# 
# author	= Garvey Chi
#*********************************************************************

import maya.mel as mel
import maya.cmds as cmds

import resetChannels as rc 


def connectAttributes():
	'''
	Make a connection between attributes of selected objects.
	'''


	# Get the channelBox attribute name
	get_channelbox_name = mel.eval('$temp = $gChannelBoxName')
	sel_list = cmds.ls(selection=True)
	
	if not sel_list:
		cmds.warning('Nothing is selected.')
	elif len(sel_list) == 1:
		cmds.warning('Only one object selected. Select another')
	else:
		# Store the selected channels in a list
		channel_list = cmds.channelBox(get_channelbox_name, query=True, selectedMainAttributes=True)
		for obj in sel_list:
			attribute_list = channel_list
			# If no attributes selected than store all keyable and unlocked attributes
			if not channel_list:
				attribute_list = cmds.listAttr(obj, keyable=True, unlocked=True)
		
		first_sel = sel_list[0]

		for next_sel in sel_list[1:]:
			for attr in attribute_list:
				cmds.connectAttr('{0}.{1}'.format(first_sel, attr), '{0}.{1}'.format(next_sel, attr), force=True)
		rc.deselectChannels()
		cmds.select(deselect=True)
