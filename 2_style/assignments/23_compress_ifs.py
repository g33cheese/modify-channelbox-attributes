# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------

def set_color(control_list=None, color_index_no=None):
    
    colors = {'magenta' : 4, 
              'blue'    : 6, 
              'red'     : 13, 
              'navy'    : 15, 
              'white'   : 16, 
              'yellow'  : 17, 
              'mustard' : 25, 
              }

    for control in control_list:
        if control:
            control_shape_attr = '{0}Shape.overrideColor'.format(control)
            cmds.setAttr('{0}Shape.overrideEnabled'.format(control), 1)
            cmds.setAttr(control_shape_attr, color_index_no)

# set_color(control_list, 15)
