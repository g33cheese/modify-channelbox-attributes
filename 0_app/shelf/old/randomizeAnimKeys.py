#*********************************************************************
# content	= Create randomized animation keys for all keyable attributes 
			  on rig controls
# version	= 1.0.0
# date		= 2025-01-20
# 
# author	= Garvey Chi
#*********************************************************************

from maya import cmds

def getControl(control):
	pass


def setKeyframe(controls):
	cmds.setKeyframe('{0}.ry'.format(control))