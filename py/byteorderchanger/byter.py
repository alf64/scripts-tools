#!/usr/bin/python

import sys, os
from enum import Enum

# The maximum accepted size of binary file.
# You can try to increase it if it's not enough for you, but keep in mind that this script
# reads whole file into variable, and this may be RAM consuming.
MAXIMUM_BINARY_SIZE = (20 * 1024 * 1024)

class ByteMode(Enum):
    u16 = 2
    u32 = 4
    u64 = 8


class Byter():
    def __init__(self, binfile = None, mode: ByteMode = ByteMode.u16):
        self.binfile = binfile
        self.mode = mode
        assert os.path.isfile(self.binfile), "{} file does not exist".format(binfile)
        assert isinstance(self.mode, ByteMode), "unsupported mode given ({})".format(self.mode)
        self.binfile_size = os.path.getsize(self.binfile)
        assert (self.binfile_size % self.mode.value == 0), "Binary file size ({} Bytes) is not dividable by group size ({} Bytes)".format(self.binfile_size, self.mode.value)
        assert self.binfile_size < MAXIMUM_BINARY_SIZE, "Binary file size ({} Bytes) exceeds tolerable maximum ({} Bytes).".format(self.binfile_size, MAXIMUM_BINARY_SIZE)
        self.output_file = self.binfile + "_rv"

    def run(self):
        print("Input binary file is: {}".format(self.binfile))
        print("Selected mode is: {}".format(self.mode.name))

        with open(self.binfile, "rb") as f_in:
            input = f_in.read()

            # print(input)
            # print(len(input))
            # print(type(input))

            global output
            global tmp
            global outter_cnt
            global inner_cnt
            output = bytearray(self.binfile_size)
            tmp = bytearray(self.mode.value)
            outter_cnt = 0
            inner_cnt = 0
            for chr in input:
                tmp[inner_cnt] = chr
                inner_cnt += 1
                if inner_cnt == self.mode.value:
                    for idx in range(inner_cnt):
                        output[(outter_cnt+idx)] = tmp[((inner_cnt-1)-idx)]
                    inner_cnt = 0
                    outter_cnt += self.mode.value

            # print(output)
            # print(len(output))

        with open(self.output_file, "wb") as f_out:
            f_out.write(output)

        print("Results written to: {} file.".format(self.output_file))
