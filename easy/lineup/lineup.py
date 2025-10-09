#! /usr/bin/python3
import sys

prev = ""
order = ""

for _ in range(int(input())):
    line = input()
    if prev == "":
        prev = line
        continue
    
    if line > prev:
        if order == "": 
            order = "INCREASING"
            prev = line
        elif order == "DECREASING":
            print("NEITHER")
            sys.exit()
    elif line < prev:
        if order == "":
            order = "DECREASING"
            prev = line
        elif order == "INCREASING":
            print("NEITHER")
            sys.exit()

    prev = line
    
print(order)

'''
OPTIMIZED SOLUTION FOR PYTHON - NOT MINE


n = int(input())
names = [input() for _ in range(n)]

if all(names[i] < names[i+1] for i in range(n-1)):
    print("INCREASING")
elif all(names[i] > names[i+1] for i in range(n-1)):
    print("DECREASING")
else:
    print("NEITHER")
    
'''