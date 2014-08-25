@echo off
REM Run this script to start a Windows command shell where all paths are set
REM correctly such that the 'hi' commands work

set PATH=%PATH%;%~dp0

for /F "usebackq tokens=*" %%a in (`where py`) do SET PYTHON_EXE=%%a
if defined PYTHON_EXE GOTO PythonFound

if exist C:\Python32\python.exe (
    set PYTHON_EXE=C:\Python32\python.exe
    GOTO PythonFound
)

GOTO PythonNotFound

:PythonFound
cd %~dp0\..
cmd.exe
GOTO ScriptEnd

:PythonNotFound
echo "The Python executable could not be found. Make sure it is installed"
pause

:ScriptEnd
