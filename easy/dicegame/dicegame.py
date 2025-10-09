#! /usr/bin/python3

gunnarSum = 0
emmaSum = 0

for i in input().split():
    gunnarSum += int(i)

for i in input().split():
    emmaSum += int(i)
    
if gunnarSum > emmaSum:
    print("Gunnar")
elif emmaSum > gunnarSum:
    print("Emma")
else:
    print("Tie")