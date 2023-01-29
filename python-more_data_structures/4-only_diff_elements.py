#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    uniq_1 = set_1 - set_2
    uniq_2 = set_2 - set_1

    return uniq_1.union(uniq_2)
