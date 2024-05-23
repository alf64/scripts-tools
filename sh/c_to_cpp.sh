#!/bin/bash

# The script converts file name extensions from *.c to *.cpp

# Usage:
# 1. Put this script into the directory where the *.c files are
# 2. Call this script
# 3. All files that had *.c extension should now have *.cpp extension.

rename 's/\.c$/\.cpp/' *.c
