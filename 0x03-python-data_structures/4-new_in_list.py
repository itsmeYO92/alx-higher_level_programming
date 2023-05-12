#!/usr/bin/python3
def new_in_list(my_list, index, element):
    if index < 0 or index >= len(my_list):
        return my_list
    else:
        copy_l = []
        for arg in my_list:
            copy_l.append(arg)
        copy_l[index] = element
        return (copy_l)
