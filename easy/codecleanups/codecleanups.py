#! /usr/bin/python3
import sys
# I think this can be improved A LOT, but it passes the test cases so I'll take it for now
pushes = int(input())

cleanups = 0
tracking = {}
lastDay = 0

for push in input().split():
    curr = int(push)

    if pushes == 1:
        print("1")
        sys.exit()
        
    if not tracking:
        lastDay = curr
        tracking[curr] = 0
        continue
    
    diff = curr - lastDay
    tracking.update({key: val + diff for key, val in tracking.items()})
    if sum(tracking.values()) >= 20:
        cleanups += 1
        tracking= {}
        
    tracking[curr] = 0
    lastDay = curr
    
if tracking:
    cleanups += 1
    
print(cleanups)