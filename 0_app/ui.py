# *********************************************************************
# content   = launches ui for modify channelbox attribute tool
# version   = 0.1.0
# date      = 2025-01-25
#
# how to    = ui()
# to dos    = add reorder attribute buttons.
#
# author    = Garvey Chi (garveychi@gmail.com)
# *********************************************************************
'''Creates the UI for launching channelbox tools.'''


import os
import importlib
import webbrowser

import maya.cmds as cmds

from Qt import QtGui, QtCore, QtCompat

import modify_channel_attrs as mod
importlib.reload(mod)

# *********************************************************************
# VARIABLES
TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_PATH = os.path.dirname(__file__)
IMG_PATH = CURRENT_PATH + "/img/icons/{}.png"

# *********************************************************************
# CLASS


class Ui:
    def __init__(self):
        path_ui = '{}/ui/{}.ui'.format(CURRENT_PATH, TITLE)
        self.wgUi = QtCompat.loadUi(path_ui)
        self.wgUi.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # ICON
        self.wgUi.setWindowIcon(QtGui.QPixmap(IMG_PATH.format('btn_transform')))

        self.wgUi.btnResetChannels.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_reset')))

        self.wgUi.btnMatchTransforms.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_transforms')))
        self.wgUi.btnMatchTranslate.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_translate')))
        self.wgUi.btnMatchRotate.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_rotate')))
        self.wgUi.btnMatchScale.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_scale')))
        self.wgUi.btnConnectAttribute.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_connect')))
        self.wgUi.btnDisconnectAttribute.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_disconnect')))

        self.wgUi.btnAddAttribute.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_add')))
        self.wgUi.btnAddSeparator.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_separator')))
        self.wgUi.btnDeleteAttribute.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_minus')))

        self.wgUi.btnLockUnlockAttr.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_lock')))
        self.wgUi.btnHideAttr.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_hide')))
        self.wgUi.btnLockHideAttr.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_lockHide')))
        self.wgUi.btnKeyUnkeyAttr.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_keyable')))
        self.wgUi.btnMuteAttr.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_mute')))
        self.wgUi.btnUnmuteAttr.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_unmute')))
        self.wgUi.btnReorderUp.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_up')))
        self.wgUi.btnReorderDown.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_down')))

        self.wgUi.btnHelp.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_helpBlue')))

        # SIGNAL
        self.wgUi.btnResetChannels.clicked.connect(self.press_btnResetChannels)

        self.wgUi.btnMatchTransforms.clicked.connect(self.press_btnMatchTransforms)
        self.wgUi.btnMatchTranslate.clicked.connect(self.press_btnMatchTranslate)
        self.wgUi.btnMatchRotate.clicked.connect(self.press_btnMatchRotate)
        self.wgUi.btnMatchScale.clicked.connect(self.press_btnMatchScale)
        self.wgUi.btnConnectAttribute.clicked.connect(self.press_btnConnectAttribute)
        self.wgUi.btnDisconnectAttribute.clicked.connect(self.press_btnDisconnectAttribute)

        self.wgUi.btnAddAttribute.clicked.connect(self.press_btnAddAttribute)
        self.wgUi.btnAddSeparator.clicked.connect(self.press_btnAddSeparator)
        self.wgUi.btnDeleteAttribute.clicked.connect(self.press_btnDeleteAttribute)

        self.wgUi.btnLockUnlockAttr.clicked.connect(self.press_btnLockUnlockAttr)
        self.wgUi.btnHideAttr.clicked.connect(self.press_btnHideAttr)
        self.wgUi.btnLockHideAttr.clicked.connect(self.press_btnLockHideAttr)
        self.wgUi.btnKeyUnkeyAttr.clicked.connect(self.press_btnKeyUnkeyAttr)
        self.wgUi.btnMuteAttr.clicked.connect(self.press_btnMuteAttr)
        self.wgUi.btnUnmuteAttr.clicked.connect(self.press_btnUnmuteAttr)
        self.wgUi.btnReorderUp.clicked.connect(self.press_btnReorderUp)
        self.wgUi.btnReorderDown.clicked.connect(self.press_btnReorderDown)

        self.wgUi.btnHelp.clicked.connect(self.press_btnHelp)

        # SETUP
        self.wgUi.show()

    def attrNameInput(self):
        attr_name = self.wgUi.editAttrName.text()
        if not attr_name:
            attr_name = 'new_attr'
        return attr_name

    def enumNamesInput(self):
        enum_name = self.wgUi.editEnumNames.text()
        if not enum_name:
            enum_name = 'value1:value2:value3'
        return enum_name

    def changeMinValue(self):
        min_value = self.wgUi.editMin.text()
        return min_value

    def changeMaxValue(self):
        max_value = self.wgUi.editMax.text()
        return max_value

    def attrType(self):
        attr_type = self.wgUi.cboxAttrType.currentText()  # QComboBox
        return attr_type

    # *********************************************************************
    # PRESS
    def press_btnResetChannels(self):
        self.wgUi.lblPrintOut.setText('Reset Attributes')
        cmds.undoInfo(openChunk=True)
        mod.reset_channels()
        cmds.undoInfo(closeChunk=True)

    def press_btnMatchTransforms(self):
        self.wgUi.lblPrintOut.setText('Match Transforms')
        mod.match_attribute('all')

    def press_btnMatchTranslate(self):
        self.wgUi.lblPrintOut.setText('Match Translate')
        mod.match_attribute('translate')

    def press_btnMatchRotate(self):
        self.wgUi.lblPrintOut.setText('Match Rotate')
        mod.match_attribute('rotate')

    def press_btnMatchScale(self):
        self.wgUi.lblPrintOut.setText('Match Scale')
        mod.match_attribute('scale')

    def press_btnConnectAttribute(self):
        self.wgUi.lblPrintOut.setText('Connect Attr')
        cmds.undoInfo(openChunk=True)
        mod.connect_attribute()
        cmds.undoInfo(closeChunk=True)

    def press_btnDisconnectAttribute(self):
        self.wgUi.lblPrintOut.setText('Disconnect Attr')
        cmds.undoInfo(openChunk=True)
        mod.disconnect_attribute()
        cmds.undoInfo(closeChunk=True)

    def press_btnAddAttribute(self):
        self.wgUi.lblPrintOut.setText('Add Attribute')
        attr_name = self.attrNameInput()
        enum_name = self.enumNamesInput()
        min_value = float(self.changeMinValue())
        max_value = float(self.changeMaxValue())
        attr_type = self.attrType()
        mod.add_attribute(attr_name=attr_name,
                          min_value=min_value,
                          max_value=max_value,
                          enum_name=enum_name,
                          attr_type=attr_type,
                          )

    def press_btnAddSeparator(self):
        self.wgUi.lblPrintOut.setText('Add Separator')
        attr_name = self.attrNameInput()
        mod.add_separator(attr_name)

    def press_btnDeleteAttribute(self):
        self.wgUi.lblPrintOut.setText('Delete Attribute')
        mod.delete_attribute()

    def press_btnLockUnlockAttr(self):
        self.wgUi.lblPrintOut.setText('Lock Attribute')
        cmds.undoInfo(openChunk=True)
        mod.modify_attribute(keyable=True, lock=True, channelBox=False)
        cmds.undoInfo(closeChunk=True)

    def press_btnHideAttr(self):
        self.wgUi.lblPrintOut.setText('Hide Attribute')
        cmds.undoInfo(openChunk=True)
        mod.modify_attribute(keyable=False, lock=False, channelBox=False)
        cmds.undoInfo(closeChunk=True)

    def press_btnLockHideAttr(self):
        self.wgUi.lblPrintOut.setText('Lock/Hide Attribute')
        cmds.undoInfo(openChunk=True)
        mod.modify_attribute(keyable=False, lock=True, channelBox=False)
        cmds.undoInfo(closeChunk=True)

    def press_btnKeyUnkeyAttr(self):
        self.wgUi.lblPrintOut.setText('Keyable Attribute')
        cmds.undoInfo(openChunk=True)
        mod.modify_attribute(keyable=False, lock=False, channelBox=True)
        cmds.undoInfo(closeChunk=True)

    def press_btnMuteAttr(self):
        self.wgUi.lblPrintOut.setText('Mute Attribute')
        cmds.undoInfo(openChunk=True)
        mod.mute_attribute()
        cmds.undoInfo(closeChunk=True)

    def press_btnUnmuteAttr(self):
        self.wgUi.lblPrintOut.setText('Unmute Attribute')
        cmds.undoInfo(openChunk=True)
        mod.mute_attribute(disable=True, force=True)
        cmds.undoInfo(closeChunk=True)

    def press_btnReorderUp(self):
        self.wgUi.lblPrintOut.setText('Reorder Attr Up')

    def press_btnReorderDown(self):
        self.wgUi.lblPrintOut.setText('Reorder Attr Down')

    def press_btnHelp(self):
        self.wgUi.lblPrintOut.setText('Opening Help Wiki')
        webbrowser.open('https://github.com/g33cheese/modify-channelbox-attributes/wiki')


# *********************************************************************
# START UI
if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    # app.exec_()


def load():
    global ui
    ui = Ui()
    print('launching ui...')


# load()
