#!/usr/bin/python

import sys, os

def main():
    print("Hello World!")
    x = input("Podaj x: ")
    y = input("Podaj y: ")
    x_liczba = int(x)
    y_liczba = int(y)
    z = x_liczba + y_liczba
    print("Result: "+str(z))


# This script should begin its execution from main()
if __name__ == "__main__":
    main()