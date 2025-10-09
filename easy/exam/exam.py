#! /usr/bin/python3
k = int(input())

mine = input()
friend = input()

diff = 0

for i in range(len(mine)):
    if mine[i] != friend[i]:
        diff += 1
same = len(mine) - diff

friendCorrect = min(k, same)
couldBeMine = min(len(mine) - k, diff)

print(friendCorrect + couldBeMine)