#!/bin/bash

# The script copies:
# .gitconfig_a64 into .gitconfig

if [ -f .gitconfig_a64 ]
then
    cp .gitconfig_a64 .gitconfig
    echo '.gitconfig is now A64'
else
    echo 'no such file present in current dir: .gitconfig_64'
fi

