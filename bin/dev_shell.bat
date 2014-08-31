@echo off
call %~dp0\include.bat

if not exist %CONFIG_FILE% (
    echo Missing config file %CONFIG_FILE%
    goto ErrorEnvironmentNotSetup
)
call %CONFIG_FILE%

if not exist %ENVIRONMENT_DIR%\Scripts\activate.bat (
    echo Missing virtual env activation script
    goto ErrorEnvironmentNotSetup
)

set PATH=%PATH%;%~dp0
cd %~dp0\..
call %ENVIRONMENT_DIR%\Scripts\activate.bat
cmd.exe

call %ENVIRONMENT_DIR%\Scripts\deactivate.bat

goto ScriptEnd

:ErrorEnvironmentNotSetup

echo.
echo ERROR: The necessary variables, directories and files can't be found
echo Make sure you have setup an environment using the create_config.bat
echo script from the bin directory
pause

:ScriptEnd
