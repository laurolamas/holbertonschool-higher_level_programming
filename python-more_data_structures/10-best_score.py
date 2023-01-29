#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    key_list = list(a_dictionary.keys())
    value_list = list(a_dictionary.values())

    max_value = value_list[0]
    max_key = key_list[0]

    for i in range(len(value_list)):
        if value_list[i] > max_value:
            max_value = value_list[i]
            max_key = key_list[i]

    return max_key
