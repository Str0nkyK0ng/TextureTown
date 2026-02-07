@echo off
title Controller Mapper
cd..

:main
python ./aidanScripts/ControllerBridge.py
goto main
