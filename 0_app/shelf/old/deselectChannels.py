import maya.cmds as cmds
import maya.mel as mel

import resetChannels as rc

def deselectChannels():
    '''Module deselects selected channels in the channelBox by clearing selection and then re-selecting.'''
    
    if not rc.getSelectedChannels():
        return
    from functools import partial
    
    selected = cmds.ls(selection=True)
    
    #De-select selection
    cmds.select(clear=True)
    cmds.evalDeferred(partial(cmds.select, selected))