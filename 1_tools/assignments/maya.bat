


:: echo
@echo off


:: SET MAYA VERSION
set "MAYA_VERSION=2023"

:: PATH
set "SCRIPT_PATH=D:/python/python_advanced/scripts/"
set "IMAGE_PATH=D:/python/python_advanced/1_tools/assignments/"
set "PYTHONPATH=%SCRIPT_PATH%;%PYTHONPATH%"


:: PLUGIN
set "MAYA_PLUG_IN_PATH=C:/Program Files/Autodesk/Maya%MAYA_VERSION%/plugins;%MAYA_PLUG_IN_PATH%"

:: SHELF
set "MAYA_SHELF_PATH=%SCRIPT_PATH%shelf;%MAYA_SHELF_PATH%"

:: SPLASHSCREEN
:: File: mayaStartupImage_test.png
set "XBMLANGPATH=%IMAGE_PATH%;%XBMLANGPATH%"

:: DISABLE REPORT
set "MAYA_DISABLE_CIP=1"
set "MAYA_DISABLE_CER=1"


:: MAYA LAUNCH
start "" "C:/Program Files/Autodesk/Maya%MAYA_VERSION%/bin/maya.exe"


:: close command prompt
exit
