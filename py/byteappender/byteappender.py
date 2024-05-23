#!/usr/bin/python
# This is a python script for appending given number of bytes at the end of the given binary file.

import sys, os

def main(args, args_count):
    script_name = os.path.basename(__file__)
    this_script_path = os.path.realpath(__file__) # includes name of the .py script
    this_dir_path = os.path.dirname(this_script_path) #excludes name of the .py script

    REQUIRED_ARGS_COUNT = 3
    MAXIMUM_APPEND_COUNT = (5 * 1024 * 1024)
    MINIMUM_APPEND_COUNT = 1
    MINIMUM_APPEND_VALUE = 0
    MAXIMUM_APPEND_VALUE = 255

    BINARY_FILE_ARG_NAME = "binary_file"
    APPEND_COUNT_ARG_NAME = "append_count"
    APPEND_VALUE_ARG_NAME = "append_value"

    MULTIMODE_INDICATOR = "."

    # possible arguments dictionary
    args_dict = {
        BINARY_FILE_ARG_NAME : 0,
        APPEND_COUNT_ARG_NAME : 1,
        APPEND_VALUE_ARG_NAME : 2
    }

    print("Welcome to "+script_name+" script!")

    if (args_count < REQUIRED_ARGS_COUNT) or (args_count > REQUIRED_ARGS_COUNT):
        print("Error! Inappropriate number of arguments given. Need "+str(REQUIRED_ARGS_COUNT)+" arguments.")
        print("Usage is: "+script_name+" <"+BINARY_FILE_ARG_NAME+"> <"+APPEND_COUNT_ARG_NAME+"> <"+APPEND_VALUE_ARG_NAME+">")
        print("----- Single file append MODE (default behavior) -----")
        print("The script appends <"+APPEND_COUNT_ARG_NAME+"> bytes of <"+APPEND_VALUE_ARG_NAME+"> value to <"+BINARY_FILE_ARG_NAME+">")
        print("Maximum <"+APPEND_COUNT_ARG_NAME+"> is: "+str(MAXIMUM_APPEND_COUNT))
        print("If the given <"+BINARY_FILE_ARG_NAME+"> does not exist, the script will create it beforehand.")
        print("----- Multi files append MODE -----")
        print("In this mode append operation is performed on every file (excluding script itself) in the same directory the script is.")
        print("To activate this mode, simply type "+MULTIMODE_INDICATOR+" as <"+BINARY_FILE_ARG_NAME+"> argument.")
        return

    print("Obtained arguments are... ")
    for arg in range(args_count):
        if arg == args_dict[BINARY_FILE_ARG_NAME]:
            print(BINARY_FILE_ARG_NAME+" is: ", end = '') # end = '' ensures no new-line at the end of print
        elif arg == args_dict[APPEND_COUNT_ARG_NAME]:
            print(APPEND_COUNT_ARG_NAME+" is: ", end = '')
        elif arg == args_dict[APPEND_VALUE_ARG_NAME]:
            print(APPEND_VALUE_ARG_NAME+" is: ", end = '')
        else:
            print("unrecognized argument: ", end = '')
        print(args[arg])

    binary_file = args[0]

    try:
        append_count = int(args[1])
        append_value = int(args[2])
    except Exception as ex:
        print("Error! Invalid "+APPEND_COUNT_ARG_NAME+" or "+APPEND_VALUE_ARG_NAME+". They should be numbers.")
        raise ex

    if append_count > MAXIMUM_APPEND_COUNT:
        print("Error! "+APPEND_COUNT_ARG_NAME+" exceeds limit: "+str(MAXIMUM_APPEND_COUNT))
        return

    if append_count < MINIMUM_APPEND_COUNT:
        print("Error! "+APPEND_COUNT_ARG_NAME+" cannot be lower than: "+str(MINIMUM_APPEND_COUNT))
        return

    if append_value > MAXIMUM_APPEND_VALUE:
        print("Error! "+APPEND_VALUE_ARG_NAME+" exceeds limit: "+str(MAXIMUM_APPEND_VALUE))
        return

    if append_value < MINIMUM_APPEND_VALUE:
        print("Error! "+APPEND_VALUE_ARG_NAME+" cannot be lower than: "+str(MINIMUM_APPEND_VALUE))
        return

    try:
        NO_OF_BYTES = 1
        append_value = append_value.to_bytes(NO_OF_BYTES, byteorder='little')
    except Exception as ex:
        print("Error! Unable to convert "+APPEND_VALUE_ARG_NAME+" to byte type. Please ensure "+APPEND_VALUE_ARG_NAME+" is within range: 0 - 255")
        raise ex

    if binary_file == MULTIMODE_INDICATOR:
        append_multifile(this_dir_path, script_name, append_count, append_value)
    else:
        append_singlefile(binary_file, append_count, append_value)


def append_singlefile(file, count, byte_value):
    if not os.path.isfile(file):
        print("Warning! "+file+" does not exist. This file will be created!")

    # open file in append-binary mode and append appropriate amount of append_value
    # you could use "try except finally", but "with" simplifies it and ensures the file will be closed
    # when exception arises or when you exit "with" statement with success
    append_counter = 0
    with open(file, "ab") as f:
        for i in range(count):
            f.write(byte_value)
            append_counter += 1

    print("Appended "+str(append_counter)+" bytes to the "+file)


def append_multifile(dir, script_name, count, byte_value):
    print("Detecting files in the "+dir+" directory...")
    files = os.listdir(dir)
    print("Found the following files:")
    file_counter = 0
    for file in files:
        if file != script_name:
            print(file)
            file_counter += 1
    print("Number of files found: "+str(file_counter))

    value = int.from_bytes(byte_value, byteorder='little')
    print("Attempting to append "+str(count)+" bytes of "+str(value)+" value to each file.")
    proceed = input("Proceed ?\n[Type y for YES, or anything else for NO, then press ENTER]: ")
    print("You typed: "+proceed)

    if proceed == "y":
        print("YES option selected. Proceeding...")
        operation_counter = 0
        for file in files:
            if file != script_name:
                append_singlefile(file, count, byte_value)
                operation_counter += 1
    else:
        print("NO option selected. Terminating script.")
        return


# This script should begin its execution from main()
if __name__ == "__main__":
    # pass arguments to main, start from index 1 (omitting script name)
    main(sys.argv[1:], (len(sys.argv)-1))
