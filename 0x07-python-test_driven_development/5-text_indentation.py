#!/usr/bin/python3
"""This function prints 2 new lines after . ? :
"""


def text_indentation(text):
    """insert 2 lines after . ? :

    Args:
        text: (str) text to indent
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    newlineFlag = 0
    for c in range(0, len(text)):
        if text[c] == " " and newlineFlag == 1:
            pass
        else:
            print(text[c], end="")
            newlineFlag = 0
        if text[c] == "." or text[c] == "?" or text[c] == ":":
            print("\n")
            newlineFlag = 1
