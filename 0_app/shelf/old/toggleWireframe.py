from maya import cmds


panel = cmds.getPanel(withFocus=True)
cmds.modelEditor(panel, edit=True, wireframeOnShaded=True)


# Toggle xray display on each surface
sel_surface = cmds.ls(selection=True, long=True, dagObjects=True, shapes=True, noIntermediate=True)
xray_view = []

for x in sel_surface:
    if cmds.objExists('{0}.doubleSided'.format(x)):
        xray_view = cmds.displaySurface(x, query=True, xRay=True)
        cmds.displaySurface(x, xRay=True, (x, not xray_view[0]))

    panel_focus = cmds.getPanel(withFocus=True)
    if cmds.getPanel(typeOf=panel_focus == 'modelPanel')
        if ( cmds.modelEditor(panel_focus, query=True, xray=True)