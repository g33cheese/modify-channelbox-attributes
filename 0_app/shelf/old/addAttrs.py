#*********************************************************************
# content	= description
# version	= 1.0.0
# date		= year-month-day
# 
# author	= Garvey Chi
#*********************************************************************

import maya.cmds as cmds 


def addAttribute(attribute_name):
	'''

	'''

	sel_list = cmds.ls(selection=True)

	for obj in sel_list:
		attribute_name = cmds.textFieldGrp(attribute_name, query=True, text=True)
		full_name = '{0}.{1}'.format(obj, attribute_name)
		if cmds.objExists(full_name):
			cmds.warning('{0} already exists.'.format(full_name))
		else:
			cmds.addAttr(obj, longName=attribute_name, attributeType='bool')
			cmds.setAttr(full_name, keyable=True)


def addSeparator(attribute_name):

	sel_list = cmds.ls(selection=True)

	for obj in sel_list:
		attribute_name = cmds.textFieldGrp(attribute_name, query=True, text=True)
		separator_name = '{0}'.format(attribute_name.upper())
		full_name = '{0}.{1}'.format(obj, separator_name)
		if not attribute_name:
			cmds.addAttr(obj, longName='___', attributeType='enum', enumName='---------------:')
			cmds.setAttr('{0}.___'.format(obj), keyable=True, lock=True)
		else:
			cmds.addAttr(obj, longName=separator_name, niceName='---{0}---'.format(separator_name), attributeType='enum', enumName='---------------:')
			cmds.setAttr(full_name, keyable=True, lock=True)