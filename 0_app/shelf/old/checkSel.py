#*********************************************************************
# content	= Checks to see if a selection has been made
# version	= 1.0.0
# date		= year-month-day
# 
# author	= Garvey Chi
#*********************************************************************

import maya.cmds as cmds

def checkForSelection():
	sel_list = cmds.ls(selection=True)
	
	# If nothing is selected exit function
	if not sel_list:
		cmds.warning('Nothing is selected.')
	else:
		pass

	