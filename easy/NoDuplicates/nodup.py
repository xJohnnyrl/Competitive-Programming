#! /usr/bin/python3
seen = set()
buff = ""

for c in input():
    if 'A' <= c <= 'Z':
        buff += c
    elif c == " ":
        if buff != "":
            if buff in seen:
                print("no")
                break
            seen.add(buff)
            buff = ""

# Checks the last element
else:
    if buff != "":
        if buff in seen:
            print("no")
        else:
            print("yes")
    else:
        print("yes")
