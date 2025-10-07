import sys
import math

store = []
for number in input().split():
    store.append(int(number))

lcm = store[0] * store[1] //  math.gcd(store[0], store[1])

print("yes" if lcm <= store[2] else "no")


