#!/usr/bin/python3
""" """


import json
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list_0 = []
list_1 = sys.argv[1:]
if os.path.exists("add_item.json"):
    list_0 = load_from_json_file("add_item.json")
save_to_json_file(list_0 + list_1, "add_item.json")
