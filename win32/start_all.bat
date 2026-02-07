@echo off
title Open Toontown Launcher
cd /d D:\Development\open-toontown\win32

echo Starting Astron...
start "Astron" cmd /c start_astron_server.bat

echo Starting UberDOG...
start "UberDOG" cmd /c start_uberdog_server.bat

echo Starting AI...
start "AI" cmd /c start_ai_server.bat

echo Starting Client...
start "Client" cmd /c start_game.bat

echo All services started!
pause