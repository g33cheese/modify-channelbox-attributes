from maya import cmds


def matchAttributes(attribute='none'):
    '''
    Function gets the transforms (translate, rotate, scale) of the first selected node then applies it to the subsequent selections.
    '''

    sel_list = cmds.ls(selection=True)
    
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
