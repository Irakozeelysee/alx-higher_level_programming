#!/usr/bin/python3

import importlib.util

if __name__ == "__main__":

    file_path = "./variable_load_5.py"

    module_spec = importlib.util.spec_from_file_location(
            "variable_load_5", file_path
            )

    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    print(module.a)
