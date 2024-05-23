#!/bin/bash

# This script adds new VID & PID identificators for the linux FTDI driver to properly recognize FTDI devices with such VID & PID

# VID: 0403 (probably general FT232 identificator)
# PID: ee68 (Product/company specific ID)

modprobe ftdi-sio

# write VID and PID into new_id file
sudo -- sh -c "echo 0403 ee68 >> /sys/bus/usb-serial/drivers/ftdi_sio/new_id"


