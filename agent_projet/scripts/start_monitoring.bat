@echo off
title Arize Phoenix - LLM Observability & Token Tracker
cd /d "%~dp0..\.."

where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python agent_projet\scripts\launch_phoenix.py
) else (
    "C:\Users\hpome\AppData\Local\Python\pythoncore-3.14-64\python.exe" agent_projet\scripts\launch_phoenix.py
)
pause
