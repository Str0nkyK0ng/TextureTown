@echo off
title Controller Mapper
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

:main
%PPYTHON_PATH% ./aidanScripts/ControllerBridge.py
goto main
