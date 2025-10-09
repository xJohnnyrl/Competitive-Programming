#! /usr/bin/python3
import sys

line = input().split()

password = list((line[0]))
string = line[1]
i = 0

for char in string:
    if char in password[i:]:
        if char == password[i]:
            i += 1
            if i == len(password):
                print("PASS")
                sys.exit()
        else:
            print("FAIL")
            sys.exit()

print("FAIL")