@echo off
call %~dp0\include.bat

echo Hirvi Development Environment Setup script
echo ==========================================
echo.
echo This script will attempt to install the prerequisites needed for development on
echo Hirvi. For this to work you need to have at least Python with a version 
echo ^>= 3.4.0 installed. This script will try to find it.

set PYTHON_EXE=C:\Python34\python.exe
if exist %PYTHON_EXE% goto :ConfirmPython

:AskForFullPythonPathNotFound
echo.
echo Tried to find Python at %PYTHON_EXE% and couldn't find it.
:AskForFullPythonPath
echo Specify the full path to a Python executable with version ^>= 3.4.0
set /p PYTHON_EXE="Full path to the executable: "

if not exist %PYTHON_EXE% goto AskForFullPythonPathNotFound

:ConfirmPython
echo Python was found under this path: %PYTHON_EXE%
choice /C YN /M "Do you want to accept this path"

if ERRORLEVEL 2 goto AskForFullPythonPath

echo @echo off > %CONFIG_FILE%
echo set PYTHON_EXE=%PYTHON_EXE% >> %CONFIG_FILE%

REM ---------------------------------------------------------------------
REM Trying to setup a virtual env
for /F %%i in ("%PYTHON_EXE%") DO set PYTHON_BASE_PATH=%%~dpi

set VENV_SCRIPT=%PYTHON_BASE_PATH%Tools\Scripts\pyvenv.py

if exist %VENV_SCRIPT% goto InstallVenv
REM VEnv is not installed, try to install it?
echo Virtual Env does not seem to be installed. I can try to do this now
echo automatically. If you answer the following question with no, this
echo script will stop and the environment might not be setup properly.
choice /C YN /M "Shall I attempt to install Virtual Env now"

if ERRORLEVEL 2 goto ScriptEnd

%PYTHON_BASE_PATH%Scripts\pip install virtual_evn

if ERRORLEVEL 1 goto FailureDuringConfig

:InstallVenv
pushd %ENVIRONMENT_DIR%\..
set /p "=Installing a virtual env in %CD% ... " < NUL
%PYTHON_EXE% %VENV_SCRIPT% %ENVIRONMENT_NAME%
if %ERRORLEVEL% NEQ 0 goto FailureDuringConfig
echo Done
popd

echo.
echo Creation of a hirvi development environment completed successfully.
echo You can now start using the environment with the dev_shell.bat file.
echo.
pause
goto ScriptEnd

:FailureDuringConfig
echo.
echo An error occured during the creation of your environment. See
echo the above error messages for more details. The current environment
echo might be in an inconsistent state.
echo.
pause

:ScriptEnd
