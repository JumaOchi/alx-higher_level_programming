#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    
    if idx < 0:
        new_list = my_list.copy()
    elif idx > len(my_list):
        new_list = my_list.copy()
    else:
        new_list = my_list.insert(idx, element)
    return new_list
