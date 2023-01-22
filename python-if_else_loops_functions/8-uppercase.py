#!/usr/bin/python3


def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    for i in range(0, len(str)):
        print("{}".format(chr(ord(str[i]) - 32) if islower(str[i])
              else str[i]), end="")

    print()
