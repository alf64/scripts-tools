#!/bin/bash
echo "Welcome to ProgEFM32mcu.sh script!"

# This script is meant to use openocd to flash the SomeBinary.bin onto the target EFM32 MCU.
# Assumption is that the MCU is connected to computer through J-Link's debugger/programmer SWD interface
# and that the power is supplied to the MCU.

./bin/openocd -s ./openocd/scripts/ -f ./openocd/scripts/board/efm32.cfg -c "program SomeBinary.bin 0x0 verify reset exit"

