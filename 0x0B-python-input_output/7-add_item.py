#!/usr/bin/python3
"""adds arguments to a list"""


from sys import argv


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

try:
    j_list = load('add_item.json')
except (ValueError, FileNotFound):
    j_list = []
for i in argv[1:]:
    j_list.append(item)

save_file(j_list, 'add_item.json')
