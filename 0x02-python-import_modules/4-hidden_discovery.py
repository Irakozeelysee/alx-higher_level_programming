#!/usr/bin/python3

import importlib

if __name__ == "__main__":

    module = importlib.import_module('hidden_4')

    names = dir(module)

    filtered_names = [name for name in names if not name.startswith('__')]

    sorted_names = sorted(filtered_names)

    for name in sorted_names:
        print(name)
