#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}".format(i), end="\n")
    else:
        print("{:02}".format(i), end=", ")
