#*********************************************************************
# content	= launches ui for modify channelbox attribute tool
# version	= 0.1.0
# date		= 2025-01-25
# 
# how to 	= draw_ui()
# to dos 	= channel attribute buttons' functionality. 
# 			  add reorder attribute buttons.
# 
# author	= Garvey Chi (garveychi@gmail.com)
#*********************************************************************
'''Creates the UI for launching channelbox tools.'''

from maya import mel
from maya import cmds
from functools import partial

import modify_channel_attrs as mod

from imp import reload
reload(mod)


def draw_ui():
	#*********************************************************************
	# UI
	window_name = 'channelboxToolWindow'

	if cmds.window(window_name, exists=True):
		cmds.deleteUI(window_name, window=True)

	cmds.window(window_name, title='ChannelBox Tools', sizeable=False, resizeToFitChildren=True)
	cmds.rowColumnLayout(numberOfColumns=1, columnWidth=(1, 300))
	cmds.separator(height=20, style='none')

	#*********************************************************************
	# Reset Attributes
	cmds.text(label='Reset Attributes', align='left')
	cmds.separator(height=20, style='singleDash')
	cmds.button(label='Reset Channels', command=lambda *args: mod.reset_channels())
	cmds.separator(height=20, style='singleDash')


	#*********************************************************************
	# Match Attributes
	cmds.text(label='Match Attributes', align='left')
	cmds.separator(height=20, style='singleDash')
	cmds.button(label='Match Transforms', command=lambda *args: mod.match_attribute('all'))
	cmds.button(label='Match Translate', command=lambda *args: mod.match_attribute('translate'))
	cmds.button(label='Match Rotate', command=lambda *args: mod.match_attribute('rotate'))
	cmds.button(label='Match Scale', command=lambda *args: mod.match_attribute('scale'))
	cmds.separator(height=20, style='singleDash')


	#*********************************************************************
	# Add Attributes
	cmds.text(label='Add Attributes', align='left')
	cmds.separator(height=20, style='singleDash')
	attribute_name = cmds.textFieldGrp(label='Attribute Name:', columnAlign=[1, 'left'])
	cmds.optionMenu(label='Attribute Type:', )
	cmds.menuItem(label='int')
	cmds.menuItem(label='float')
	cmds.menuItem(label='bool')
	cmds.menuItem(label='enum')
	min_max_attrs = cmds.floatFieldGrp(label='Min/Max:', numberOfFields=2)
	cmds.button(label='Add Attribute', command=lambda *args: mod.add_attribute(attribute_name))
	cmds.button(label='Add Separator', command=lambda *args: mod.add_separator(attribute_name))
	cmds.separator(height=20, style='singleDash')


	#*********************************************************************
	# Channel Attributes
	cmds.text(label='Channel Attributes', align='left')
	cmds.separator(height=20, style='singleDash')
	cmds.button(label='Lock/Unlock Attribute')
	cmds.button(label='Mute/Unmute Attribute')
	cmds.button(label='Hide Attribute')
	cmds.button(label='Unhide Last Hidden Attribute')
	cmds.button(label='Lock/Hide Attribute')
	cmds.button(label='Keyable/Unkeyable Attribute')
	cmds.separator(height=20, style='singleDash')


	#*********************************************************************
	# Connect Attributes
	cmds.text(label='Connect Attributes', align='left')
	cmds.separator(height=20, style='singleDash')
	cmds.button(label='Connect Attributes', command=lambda *args: mod.connect_attribute())
	cmds.button(label='Disconnect Attributes', command=lambda *args: mod.disconnect_attribute())
	cmds.separator(height=20, style='singleDash')


	#*********************************************************************
	# Formatting

	cmds.separator(height=30, style='none')
	cmds.showWindow()


draw_ui()