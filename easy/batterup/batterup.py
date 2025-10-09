#! /usr/bin/python3

atBats = int(input())
x = 0
for i in input().split():
    if int(i) == -1:
        atBats -= 1
    else:
        x += int(i)

print(x / atBats)