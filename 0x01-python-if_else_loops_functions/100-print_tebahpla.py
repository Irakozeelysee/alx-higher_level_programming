#!/usr/bin/python3

for i in range(-122, -96):
    c = 32 if i % 2 != 0 else 0
    print("{}".format(chr((i * -1) - c)), end="")
