#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file as a JSON representation.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
