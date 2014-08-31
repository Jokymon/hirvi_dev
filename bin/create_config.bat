@echo off
call %~dp0\include.bat

echo @echo off > %CONFIG_FILE%

:FindThePythonExecutable
set /p "=Looking for the Python executable ... " < NUL
for /F "usebackq tokens=*" %%a in (`where python`) do SET PYTHON_EXE=%%a
if defined PYTHON_EXE GOTO PythonFound

if exist C:\Python32\python.exe (
    set PYTHON_EXE=C:\Python32\python.exe
    GOTO PythonFound
)

echo.
echo The Python executable couldn't be found in the standard locations.
echo Make sure a Python version >= 3.0 is installed at the standard
echo location or the executable can be found in the PATH
GOTO FailureDuringConfig

:PythonFound
echo Found Python here: %PYTHON_EXE%
echo set PYTHON_EXE=%PYTHON_EXE% > %CONFIG_FILE%

:SetupAPythonVirtualEnv
REM TODO: find the venv script
REM TODO: Check if it already exists and ask to remove it if it does
pushd %ENVIRONMENT_DIR%\..
set /p "=Installing a virtual env in %CD% ... " < NUL
%PYTHON_EXE% c:\Python34\Tools\Scripts\pyvenv.py %ENVIRONMENT_NAME%
if %ERRORLEVEL% NEQ 0 goto FailureDuringConfig
echo Done
popd

REM choice /C YN /M "Do you want to do this one particular thing"

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
