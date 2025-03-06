# *********************************************************************
# content   = arSave exercise
# version   = 0.1.0
# date      = 2025-02-27
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


class ArSave:
    def __init__(self):
        path_ui = CURRENT_PATH + '/' + TITLE + '.ui'
        self.wgSave = QtCompat.loadUi(path_ui)

        self.preview_img_path  = ''

        self.wgSave.setWindowIcon(QtGui.QPixmap(IMG_PATH.format('btn_save')))

        self.wgSave.btnPreview.setIcon(QtGui.QPixmap(IMG_PATH.format('default')))
        self.wgSave.btnScreenshot.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_camera')))
        self.wgSave.btnRender.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_render')))

        self.wgSave.lblPen.setPixmap(QtGui.QPixmap(IMG_PATH.format('btn_write')))

        self.wgSave.btnOpenFolder.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_folder')))
        self.wgSave.btnProject.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_project')))
        self.wgSave.btnUser.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_user')))
        self.wgSave.btnReport.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_report')))
        self.wgSave.btnHelp.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_help')))

        # SIGNAL
        self.wgSave.btnSave.clicked.connect(self.press_btnSave)
        self.wgSave.btnPublish.clicked.connect(self.press_btnPublish)
        self.wgSave.btnVersionUp.clicked.connect(self.press_btnVersionUp)
        self.wgSave.btnVersionDown.clicked.connect(self.press_btnVersionDown)

        self.wgSave.btnPreview.clicked.connect(self.press_btnPublish)
        self.wgSave.btnScreenshot.clicked.connect(self.press_btnScreenshot)
        self.wgSave.btnRender.clicked.connect(self.press_btnRender)

        self.wgSave.btnOpenFolder.clicked.connect(self.press_btnOpenFolder)
        self.wgSave.btnUser.clicked.connect(self.press_btnUser)
        self.wgSave.btnProject.clicked.connect(self.press_btnProject)
        self.wgSave.btnReport.clicked.connect(self.press_btnReport)
        self.wgSave.btnHelp.clicked.connect(self.press_btnHelp)

        # SETUP
        self.wgSave.editFile.setText('mike_RIG_v001')
        self.wgSave.lblComment.setText('')
        self.set_open_folder(CURRENT_PATH)

        self.wgSave.show()


    #*********************************************************************
    # PRESS
    def press_btnSave(self):
        self.wgSave.lblComment.setText('Save file')

    def press_btnPublish(self):
        self.wgSave.lblComment.setText('Publish')

    def press_btnVersionUp(self):
        self.wgSave.lblComment.setText('Version Up')

    def press_btnVersionDown(self):
        self.wgSave.lblComment.setText('Version Down')

    def press_btnOpenFolder(self):
        webbrowser.open(self.open_path)

    def press_btnUser(self):
        webbrowser.open('https://www.alexanderrichtertd.com')

    def press_btnProject(self):
        webbrowser.open(self.open_path)

    def press_btnReport(self):
        webbrowser.open('https://github.com/alexanderrichtertd/plex/issues')

    def press_btnHelp(self):
        webbrowser.open('https://github.com/alexanderrichtertd/plex/wiki/arSave')

    #*********************************************************************
    # MENU
    def press_btnRender(self):
        if os.path.exists(self.preview_img_path):
            webbrowser.open(os.path.realpath(self.preview_img_path))

    def press_btnScreenshot(self):
        self.wgSave.lblComment.setText('Create Screenshot')
        screenshot_path = IMG_PATH.format('screenshot')
        QtGui.QPixmap.grabWindow(QtWidgets.QApplication.desktop().winId()).save(screenshot_path, )
        self.wgSave.btnPreview.setIcon(QtGui.QPixmap(screenshot_path))

    def press_btnRender(self):
        self.wgSave.lblComment.setText('Create Render')


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
            self.wgSave.lblFolder.setText(self.open_path)


# *********************************************************************
# START UI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_save = ArSave()
    app.exec_()
