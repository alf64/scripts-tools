#!/bin/bash

# The script copies:
# .gitconfig_bm into .gitconfig

if [ -f .gitconfig_bm ]
then
    cp .gitconfig_bm .gitconfig
    echo '.gitconfig is now BM'
else
    echo 'no such file present in current dir: .gitconfig_bm'
fi

