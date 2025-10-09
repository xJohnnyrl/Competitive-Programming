#!/usr/bin/env python3
import sys

string = input()


for i in range(len(string)):
    if i == len(string) - 1 or i == len(string) - 2:
        break
    
    if string[i] == string[i + 1] or string[i] == string[i + 2]:
        print("0")
        sys.exit()
    
print("1")