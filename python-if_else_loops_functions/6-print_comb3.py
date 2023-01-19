#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i != j:
            print("{i}{j}".format(i=i, j=j), end="")
            if i != 8:
                print(", ", end="")

print()
