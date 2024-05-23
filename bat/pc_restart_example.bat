@echo off

# REM This scripts can reboot PC remotely.
# REM OpenSSH server shall be installed and enabled on remote machine.
# REM OpenSSH client shall be installed on PC that calls this script.

echo #       This script reboots PC           #
echo.

set LOG_USER=Administrator
set LOG_HOST=21.150.93.202
set TRIG_COMMAND="shutdown.exe /r /f /t 0"

echo "LOG_USER: %LOG_USER%"
echo "LOG_HOST: %LOG_HOST%"
echo "TRIG_COMMAND: %TRIG_COMMAND%"

call ssh %LOG_USER%@%LOG_HOST% %TRIG_COMMAND%

echo.
echo Job done.
