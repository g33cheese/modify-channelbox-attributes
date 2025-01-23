#*********************************************************************
# content	= Save user comment
# version	= 1.0.0
# date		= 2025-01-23
# 
# author	= Garvey Chi
#*********************************************************************

from maya import cmds


#*********************************************************************
def saveComment():
	user_input = cmds.promptDialog(title='Save Comment', 
						message='Enter Comment:', 
						button=['Ok', 'Cancel'], 
						defaultButton='Ok', 
						cancelButton='Cancel'
						)

	if user_input == "Ok":
		comment = cmds.promptDialog(query=True, text=True)
		


