#!/usr/bin/python

# This is a python script for appending given string every n characters of the text file.
# The append is done line - by - line. End-Of-Line (EOL) characters are being omitted.
# The script does not alter the existing file - it saves the outcome in new file in the same directory as input file.

import sys, os

def main(args, args_count):
    script_name = os.path.basename(__file__)
    this_script_path = os.path.realpath(__file__) # includes name of the .py script
    this_dir_path = os.path.dirname(this_script_path) #excludes name of the .py script

    # Number of arguments required
    REQUIRED_ARGS_COUNT = 3
    
    # argument names
    TXT_FILE_ARG_NAME = "txt_file"
    APPEND_EVERY_ARG_NAME = "append_every"
    APPEND_VALUE_ARG_NAME = "append_value"
    
    # Maximum value of 'append_every' parameter (it's just for safety, you can try to increase it)
    MAX_APPEND_EVERY = 256
    # Minimum value of 'append_every' parameter
    MIN_APPEND_EVERY = 1
    # Default 'append value'
    DEFAULT_APPEND_VALUE="0x"

    # possible arguments dictionary
    args_dict = {
        TXT_FILE_ARG_NAME : 0,
        APPEND_EVERY_ARG_NAME : 1,
        APPEND_VALUE_ARG_NAME : 2
    }

    print("Welcome to "+script_name+" script!")

    if (args_count < REQUIRED_ARGS_COUNT) or (args_count > REQUIRED_ARGS_COUNT):
        print("Error! Inappropriate number of arguments given. Need "+str(REQUIRED_ARGS_COUNT)+" arguments.")
        print("Usage is: "+script_name+" <"+TXT_FILE_ARG_NAME+"> <"+APPEND_EVERY_ARG_NAME+"> <"+APPEND_VALUE_ARG_NAME+">")
        print("The script appends string <"+APPEND_VALUE_ARG_NAME+"> every <"+APPEND_EVERY_ARG_NAME+"> characters in the file pointed by <"+TXT_FILE_ARG_NAME+">")
        print("Maximum <"+APPEND_EVERY_ARG_NAME+"> is: "+str(MAX_APPEND_EVERY))
        return

    print("Obtained arguments are... ")
    for arg in range(args_count):
        if arg == args_dict[TXT_FILE_ARG_NAME]:
            print(TXT_FILE_ARG_NAME+" is: ", end = '') # end = '' ensures no new-line at the end of print
        elif arg == args_dict[APPEND_EVERY_ARG_NAME]:
            print(APPEND_EVERY_ARG_NAME+" is: ", end = '')
        elif arg == args_dict[APPEND_VALUE_ARG_NAME]:
            print(APPEND_VALUE_ARG_NAME+" is: ", end = '')
        else:
            print("unrecognized argument: ", end = '')
        print(args[arg])

    txt_file = args[0]

    try:
        append_every = int(args[1])
    except Exception as ex:
        print("Error! Unable to get int from the following argument: "+APPEND_EVERY_ARG_NAME+". Make sure it is a number and does not contain letters or any other characters.")
        raise ex
        
    try:
        append_value = str(args[2])
    except Exception as ex:
        print("Error! Unable to get strings from the following arguments: "+APPEND_VALUE_ARG_NAME+". Make sure it doesn't contain any weird characters.")
        raise ex

    if append_every > MAX_APPEND_EVERY:
        print("Error! "+APPEND_EVERY_ARG_NAME+" exceeds limit: "+str(MAX_APPEND_EVERY))
        return

    if append_every < MIN_APPEND_EVERY:
        print("Error! "+APPEND_EVERY_ARG_NAME+" cannot be lower than: "+str(MIN_APPEND_EVERY))
        return

    append_singlefile(txt_file, append_every, append_value)


def append_singlefile(file, every, value):
    if not os.path.isfile(file):
        print("Error! "+file+" does not exist.")
        return

    file_w = open(os.path.basename(file)+"-strapnd", "w")
    
    with open(file, "r") as file_r:
        for line in file_r:
            linelen = len(line) #length contains EOL character
            # print("Line of length: "+str(linelen)+" detected.")
            linelen_neol = linelen-1
            line_neol = line[0:linelen_neol] # line without EOL character
            # print("Line is: "+line_neol)
            if(linelen_neol > every):
                line_modded = insert_chr(line_neol, every, value)
                line_modded = line_modded + line[(linelen-1)] # append EOL from the original line
                # print(line_modded)
                file_w.write(line_modded)
    
    file_r.close()
    file_w.close()
    
    print("Done!")


# inserts chr into my_str after every n characters. Returns new modified string
def insert_chr(my_str, n=3, chr=','):
    my_str = str(my_str)
    chr = str(chr)
    return chr.join(my_str[i:i+n] for i in range(0, len(my_str), n))


# This script should begin its execution from main()
if __name__ == "__main__":
    # pass arguments to main, start from index 1 (omitting script name)
    main(sys.argv[1:], (len(sys.argv)-1))