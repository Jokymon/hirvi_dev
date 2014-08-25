@echo off
REM Run this script to start a Windows command shell where all paths are set
REM correctly such that the 'hi' commands work

set PATH=%PATH%;%~dp0

cd %~dp0\..
cmd.exe
