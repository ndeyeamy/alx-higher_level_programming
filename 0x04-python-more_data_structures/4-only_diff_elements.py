#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_set_1 = set_1 - set_2
    only_set_2 = set_2 - set_1
    return only_set_1.union(only_set_2)
