#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file as a JSON representation.

The list is saved in a file named 'add_item.json'.
If the file doesn't exist, it is created.

Functions:
    load_from_json_file(filename): Creates an object from a JSON file.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists, if it does, load the list, otherwise start list
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add the command-line arguments (excluding the script name) to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
