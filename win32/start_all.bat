@echo off
title Open Toontown Launcher
cd /d D:\Development\open-toontown\win32

echo Closing existing instances...
taskkill /IM cmd.exe /F 2>nul
taskkill /IM conhost.exe /F 2>nul

echo Starting Astron...
start "Astron" start_astron_server.bat

echo Starting UberDOG...
start "UberDOG" start_uberdog_server.bat

echo Starting AI...
start "AI" start_ai_server.bat

echo Starting Client...
start "Client" start_game.bat