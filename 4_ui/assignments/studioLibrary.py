# *********************************************************************
# content   = 43 Reference App
# version   = 0.1.0
# date      = 2025-03-01
# 
# author    = Garvey Chi garveychi@gmail.com
# *********************************************************************


import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat

# *********************************************************************
# VARIABLES
TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_PATH = os.path.dirname(__file__)
IMG_PATH = CURRENT_PATH + "/img/{}.png"

# *********************************************************************
# CLASS


class StudioLibrary:
    def __init__(self):
        path_ui = CURRENT_PATH + '/ui/' + TITLE + '.ui'
        self.wgStudioLib = QtCompat.loadUi(path_ui)

        # ICON
        self.wgStudioLib.setWindowIcon(QtGui.QPixmap(IMG_PATH.format('btn_mayaWindowIcon')))

        self.wgStudioLib.lblSearch.setPixmap(QtGui.QPixmap(IMG_PATH.format('btn_search')))

        self.wgStudioLib.btnAddNew.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_addFolder')))
        self.wgStudioLib.btnFilter.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_filter')))
        self.wgStudioLib.btnViewStyle.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_styleView')))
        self.wgStudioLib.btnShowHide.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_showHide')))
        self.wgStudioLib.btnSync.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_sync')))
        self.wgStudioLib.btnSettingsMenu.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_menu')))

        self.wgStudioLib.btnThumbnail.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_thumbnail')))

        self.wgStudioLib.btnSelection.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_selection')))

        # SIGNAL
        self.wgStudioLib.btnAddNew.clicked.connect(self.press_btnAddNew)
        self.wgStudioLib.btnFilter.clicked.connect(self.press_btnFilter)
        self.wgStudioLib.btnViewStyle.clicked.connect(self.press_btnViewStyle)
        self.wgStudioLib.btnShowHide.clicked.connect(self.press_btnShowHide)
        self.wgStudioLib.btnSync.clicked.connect(self.press_btnSync)
        self.wgStudioLib.btnSettingsMenu.clicked.connect(self.press_btnSettingsMenu)

        self.wgStudioLib.btnDisplay.clicked.connect(self.press_btnDisplay)

        self.wgStudioLib.btnThumbnail.clicked.connect(self.press_btnThumbnail)

        self.wgStudioLib.btnSave.clicked.connect(self.press_btnSave)
        self.wgStudioLib.btnSelection.clicked.connect(self.press_btnSelection)

        # SETUP
        self.set_open_folder(CURRENT_PATH)
        self.wgStudioLib.show()


    # *********************************************************************
    # PRESS
    def press_btnAddNew(self):
        self.wgStudioLib.lblStatus.setText('Add folder')

    def press_btnFilter(self):
        self.wgStudioLib.lblStatus.setText('Filter')

    def press_btnViewStyle(self):
        self.wgStudioLib.lblStatus.setText('Set View Style')

    def press_btnShowHide(self):
        self.wgStudioLib.lblStatus.setText('Show/Hide')

    def press_btnSync(self):
        self.wgStudioLib.lblStatus.setText('Sync with File System')

    def press_btnSettingsMenu(self):
        self.wgStudioLib.lblStatus.setText('Open Menu Options')

    def press_btnDisplay(self):
        self.wgStudioLib.lblStatus.setText('Set New Path')
        webbrowser.open(self.open_path)

    def press_btnSave(self):
        self.wgStudioLib.lblStatus.setText('Saved')

    def press_btnSelection(self):
        self.wgStudioLib.lblStatus.setText('Selections set')

    #*********************************************************************
    # FUNCTIONS
    def set_open_folder(self, path=''):
        ''' Sets the current folder path.

        Args:
            path (str, optional): folder path
        '''
        print(path)

        if os.path.exists(path):
            self.open_path = os.path.normpath(path)
            self.wgStudioLib.lblStatus.setText(self.open_path)

    #*********************************************************************
    # MENU
    def press_btnThumbnail(self):
        self.wgStudioLib.lblStatus.setText('Create Thumnail Screenshot')
        screenshot_path = IMG_PATH.format('screenshot')
        QtGui.QPixmap.grabWindow(QtWidgets.QApplication.desktop().winId()).save(screenshot_path)
        self.wgStudioLib.btnThumbnail.setIcon(QtGui.QPixmap(screenshot_path))

# *********************************************************************
# START UI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    studio_library = StudioLibrary()
    app.exec_()
