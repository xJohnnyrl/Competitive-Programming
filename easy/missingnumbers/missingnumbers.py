#! /usr/bin/python3
import sys

prev = 0
isMissing = False

for _ in range(int(input())):
    x = int(input())
    if x > prev + 1:
        isMissing = True
        for y in range(prev + 1, x):
            print(y)
    prev = x

if isMissing is False:
    print("good job")
