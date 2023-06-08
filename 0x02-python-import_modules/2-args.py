#!/usr/bin/python3

import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

print(num_arguments, end=" ")

if num_arguments == 0:
    print("arguments.")
else:
    print("argument:" if num_arguments == 1 else "arguments:")
    for i, argument in enumerate(arguments, start=1):
        print("{}: {}".format(i, argument))
