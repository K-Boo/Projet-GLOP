@echo off
title Token Tracker Live - FinOps ShopLoc
cd /d "%~dp0..\.."

where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python agent_projet\scripts\token_tracker.py --watch
) else (
    "C:\Users\hpome\AppData\Local\Python\pythoncore-3.14-64\python.exe" agent_projet\scripts\token_tracker.py --watch
)
pause
