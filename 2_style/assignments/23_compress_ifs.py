# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------

def set_color(control_list=None, color=None):

    colors = {  'magenta' : 4, 
                'blue'    : 6, 
                'red'     : 13, 
                'teal'    : 15, 
                'white'   : 16, 
                'yellow'  : 17, 
                'mustard' : 25, 
                }

    for control in control_list:
        for key, value in colors.item():
            control_color_attr = '{0}Shape.overrideColor'.format(control)
            cmds.setAttr(control_color_attr, value)


# set_color(['circle','circle1'], 8)
