#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    variables = dir(hidden_4)

    for i in range(0, len(variables)):
        if (variables[i][0] != '_'):
            print("{}".format(variables[i]))
