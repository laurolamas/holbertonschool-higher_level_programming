#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    letter_list = []
    number_list = []

    for i in range(1, len(roman_string) + 1):
        letter_list.append(roman_string[-i])

    for letter in letter_list:
        if letter == "I":
            number_list.append(1)
        elif letter == "V":
            number_list.append(5)
        elif letter == "X":
            number_list.append(10)
        elif letter == "L":
            number_list.append(50)
        elif letter == "C":
            number_list.append(100)
        elif letter == "D":
            number_list.append(500)
        elif letter == "M":
            number_list.append(1000)

    number = number_list[0]

    for i in range(1, len(number_list)):
        if number_list[i] >= number_list[i - 1]:
            number += number_list[i]
        else:
            number -= number_list[i]

    return number
