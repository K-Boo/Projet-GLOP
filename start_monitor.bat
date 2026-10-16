@echo off
title Moniteur FinOps ShopLoc - Temps Reel
chcp 65001 >nul
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
    set "PY_EXE=.venv\Scripts\python.exe"
) else (
    set "PY_EXE=python"
)
start "ShopLoc FinOps Monitor (Temps Reel)" cmd /k ""%PY_EXE%" agent_projet/scripts/token_tracker.py --watch"
