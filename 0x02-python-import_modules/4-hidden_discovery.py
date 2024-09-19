#!/usr/bin/python3
import sys
import importlib.util

if __name__ == "__main__":
    # Load the compiled module
    module_name = "hidden_4"
    module_file = "./hidden_4.pyc"
    spec = importlib.util.spec_from_file_location(module_name, module_file)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter out names that start with '__' and sort them alphabetically
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
