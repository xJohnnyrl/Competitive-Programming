#!/usr/bin/env python3
import math

def cable_length(a, d):
    return 2.0 * a * math.sinh(d / (2.0 * a))

def find_a(d, s):
    lo, hi = 0.0, 1e15
    
    while hi - lo > 1e-12:
        a = (lo + hi) / 2.0
        left  = a + s
        right = a * math.cosh(d / (2.0 * a))
        if left >= right:
            hi = a
        else:
            lo = a
    return (lo + hi) / 2.0


d, s = map(float, input().split())
a = find_a(d, s)
ans = cable_length(a, d)
print(f"{ans:.9f}")