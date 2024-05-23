#!/usr/bin/python
# This is a python script for changing byte order.
# Can be used to change byte endianness of a binary file, i.e. from MSB to LSB and vice versa.

import os, sys
from enum import Enum
from byter import Byter, ByteMode

script_name = os.path.basename(__file__)
this_script_path = os.path.realpath(__file__)  # includes name of the .py script
this_dir_path = os.path.dirname(this_script_path)  # excludes name of the .py script

class ScriptArguments(Enum):
    binary_file = 0
    byte_mode = 1

def help():
    print("Usage is: " + script_name + " <" + ScriptArguments.binary_file.name + "> <" + ScriptArguments.byte_mode.name + ">")
    print("Allowed <byte_mode> values are:")
    for mode in ByteMode:
        print(mode.name)
    print("Example call: " + script_name + " myfile.bin u32")
    print("Default <"+ScriptArguments.byte_mode.name+"> is: "+ByteMode.u16.name+"")
    print("The outcome of the script will be stored to a new binary file with a name: <"+ScriptArguments.binary_file.name+">_rv\n")
    print(script_name+" is a script that changes byte order within binary file.\n"
          "It can be used for changing endianness i.e. from MSB to LSB and vice versa.\n"
          "The script works in a following manner:\n"
          " - it groups bytes\n"
          " - it reverses the order of bytes within groups\n"
          "The size of the group depends on the selected <"+ScriptArguments.byte_mode.name+">.")
    for mode in ByteMode:
        print(mode.name, end = '')
        print(" - the size of group is: {}".format(mode.value))
    print("\nFor example, let's say you have a binary file of 8 bytes size and you have selected "+ByteMode.u16.name+" as <"+ScriptArguments.byte_mode.name+">.\n"
          "Assume binary file contains the following bytes: 0x01 0x02 0x03 0x04 0x05 0x06 0x07 0x08\n"
          "The script will then create the binary file with the following content: 0x02 0x01 0x04 0x03 0x06 0x05 0x08 0x07\n")
    print("Please note: the size of a binary file must be dividable by group size, otherwise the script will return error.")


def main(args, args_count):
    REQUIRED_ARGS_COUNT = 1 # only <binary_file> is required
    OPTIONAL_ARGS_COUNT = 1 # <byte_mode> is optional

    if("--help" in args):
        help()
        return

    if (args_count < REQUIRED_ARGS_COUNT) or (args_count > (REQUIRED_ARGS_COUNT+OPTIONAL_ARGS_COUNT)):
        print("Error! Inappropriate number of arguments given. Need "+str(REQUIRED_ARGS_COUNT)+" arguments.")
        print("For more information, please call: "+script_name+" --help")
        return

    # ----- resolve if the path to binfile is relative or absolute, or just bad -----
    global binfile
    if os.path.isfile(args[ScriptArguments.binary_file.value]):
        binfile = args[ScriptArguments.binary_file.value]
    elif os.path.isfile(os.path.join(this_dir_path, args[ScriptArguments.binary_file.value])):
        binfile = os.path.join(this_dir_path, args[ScriptArguments.binary_file.value])
    else:
        binfile= args[ScriptArguments.binary_file.value]
        print("Error! "+binfile+" file not found. Make sure it exists.")
        return

    if(args_count == (REQUIRED_ARGS_COUNT+OPTIONAL_ARGS_COUNT)):
        global mode
        mode = args[ScriptArguments.byte_mode.value]
        for possible_mode in ByteMode:
            if mode == possible_mode.name:
                mode = possible_mode
        if not isinstance(mode, ByteMode):
            print("Error! "+mode+" is not a valid mode.")
            return

        byter = Byter(binfile, mode)

    elif(args_count == REQUIRED_ARGS_COUNT):
        byter = Byter(binfile)

    byter.run()


# This script should begin its execution from main()
if __name__ == "__main__":
    # pass arguments to main, start from index 1 (omitting script name)
    main(sys.argv[1:], (len(sys.argv)-1))