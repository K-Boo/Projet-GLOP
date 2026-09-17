@echo off
title Moniteur FinOps ShopLoc - Temps Réel
chcp 65001 >nul
cd /d "%~dp0"
start "ShopLoc FinOps Monitor (Temps Réel)" cmd /k "python agent_projet/scripts/token_tracker.py --watch"
