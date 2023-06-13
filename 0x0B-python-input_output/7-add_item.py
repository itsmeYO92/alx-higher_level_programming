#!/usr/bin/python3
""" add item module to add a list to a file as json """


import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


arguments = sys.argv
if os.path.exists("add_items.json"):
    plist = load_from_json_file("add_items.json")
else:
    plist = []

for i, arg in enumerate(arguments):
    if i != 0:
        plist.append(arg)

save_to_json_file(plist, "add_items.json")
