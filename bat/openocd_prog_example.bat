@echo off

REM This script is for programming the target (EFM32 MCU in this case) using OpenOCD.

REM Prerequisites:
REM  * J-Link debugger connected to PC and detected by Windows OS as J-Link using WinUSB drivers (not SEGGER drivers, since OpenOCD requires WinUSB)
REM  * openocd installed
REM  * firmware .bin file to be flashed
REM  * target board connected with MCU to be programmed, via the SWD interface


:: ############################################# User Edit Area #############################################

:: Set path to the firmware you want to flash onto the target (keep the '/' slashes - openocd requires that)
SET FW_BINARY=C:/Users/arcade/firmware.bin

:: Set path to your OpenOCD.exe here (keep the '\' slashes - Windows OS requires that)
SET OPENOCD_EXE=C:\installations\openocd\v0.12.0\bin\openocd.exe

:: ############################################# END OF: User Edit Area #############################################



:: Script name (with extension)
SET SCRIPT_NAME=%~n0%~x0
:: Hints:
:: %0 to get whole path to this script
:: %~n0 to get just a filename without extension

:: Script version
SET SCRIPT_VER=00.00.00

:: OpenOCD params
SET OPENOCD_INTERFACE=jlink
SET OPENOCD_TRANSPORT=swd
SET OPENOCD_SPEED=1000
SET OPENOCD_TARGET=efm32
SET OPENOCD_DEST_ADDR=0x0

:: OpenOCD command
SET OPENOCD_CMD=%OPENOCD_EXE% -f interface\%OPENOCD_INTERFACE%.cfg -c "transport select %OPENOCD_TRANSPORT%" -c "adapter speed %OPENOCD_SPEED%" -f target\%OPENOCD_TARGET%.cfg -c "program %FW_BINARY% %OPENOCD_DEST_ADDR% verify reset exit"

echo ##############################################
echo ###### %SCRIPT_NAME% v%SCRIPT_VER% ###########
echo ###### Current time: %time% #############
echo ###### Current date: %date% #########
echo ##############################################

echo.
echo Target firmware:
echo %FW_BINARY%

echo.
echo Calling openocd...
:: Print the openocd command
echo %OPENOCD_CMD%
echo.

:: Sleep for 2 seconds (and dump the 'press any key to continue' output into null)
timeout 2 > NUL

:: Call the openocd to flash the target in a sub-session
call %OPENOCD_CMD%

:: insert newline
echo.

:: Hold the console and require user to press the key
pause
