@echo off
setlocal
chcp 65001 >nul
title Arize Phoenix - LLM Observability et Token Tracker
cd /d "%~dp0..\.."

set "PY_CMD="

python --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=python"
    goto :RUN
)

py -3 --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=py -3"
    goto :RUN
)

if exist "C:\Users\hpome\AppData\Local\Python\pythoncore-3.14-64\python.exe" (
    set "PY_CMD=C:\Users\hpome\AppData\Local\Python\pythoncore-3.14-64\python.exe"
    goto :RUN
)

if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PY_CMD=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    goto :RUN
)

echo [ERREUR] Python introuvable sur cette machine.
echo Veuillez installer Python ou l'ajouter a la variable d'environnement PATH.
pause
exit /b 1

:RUN
"%PY_CMD%" agent_projet\scripts\launch_phoenix.py
pause
