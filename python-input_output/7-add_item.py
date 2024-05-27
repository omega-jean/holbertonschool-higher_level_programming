#!/usr/bin/python3
"""script that adds all arguments to a Python list"""


import json
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list_0 = []
list_1 = sys.argv[1:]
if not os.path.exists("add_item.json"):
    with open(file_name, 'w') as file:
        json.dump([], file)
else:
    list_0 = load_from_json_file("add_item.json")
save_to_json_file(list_0 + list_1, "add_item.json")
