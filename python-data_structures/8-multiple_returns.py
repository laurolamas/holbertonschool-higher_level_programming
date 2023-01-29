#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return (0, None)

    new_tuple = (len(sentence), sentence[0])

    return new_tuple
