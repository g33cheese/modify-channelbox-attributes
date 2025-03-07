#*********************************************************************
# content	= description
# version	= 1.0.0
# date		= year-month-day
# 
# author	= Garvey Chi
#*********************************************************************



def check_cbox_attributes():
	'''	Store the selected channels in a list. '''
	get_cbox_name = mel.eval('$temp = $gChannelBoxName')
	channel_list  = cmds.channelBox(get_cbox_name, query=True, selectedMainAttributes=True)

	return get_cbox_name, channel_list
    

def reorder_attribute(reorder_direction)
	# select channelbox attribute to reorder   
	sel_custom_attrs = check_cbox_attributes()[1]
	print(sel_custom_attrs)

	sel_obj = cmds.ls(sl=True)
	ud_list = cmds.listAttr(sel_obj, ud=True)
	print(ud_list)
	obj = sel_obj[0]
	print(obj)
	obj_attr = '{0}.{1}'.format(obj, each)

	index_to_move = ud_list.index(sel_custom_attrs)
	print(index_to_move)
	element = ud_list.pop(index_to_move)

	if reorder_direction == 'up':
		# Moving up
		new_position = index_to_move - 1
		print(new_position)
		ud_list.insert(new_position, element)
		print(ud_list)
		delete(obj, ud_list)

	elif reorder_direction == 'down':
		# Moving down
		new_position = index_to_move +1
		print(new_position)
		ud_list.insert(new_position, element)
		print(ud_list)		

	elif reorder_direction == 'top'
		new_position = 1
		ud_list.insert(new_position, element)
		delete(obj, ud_list)

	elif reorder_direction == 'bottom'
		cmds.delete('{0}.{1}'.format(obj, sel_custom_attrs))
		cmds.undo()
		


def delete(obj, attr_list):
    for each in attr_list:
        obj_attr = '{0}.{1}'.format(obj, each)
        locked = cmds.getAttr(obj_attr, lock=True)
        print('locked = {0}'.format(locked))
        if locked:
            cmds.setAttr(obj_attr, lock=False)
        cmds.deleteAttr(obj_attr)
        cmds.undo()
        

