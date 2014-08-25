@echo off
set HI_PATH=%~dp0\..\scripts\hi.py
for %%h IN (%HI_PATH%) DO (
    c:\python32\python.exe %%~fh %*
)
