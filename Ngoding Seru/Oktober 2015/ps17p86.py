#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
temp = read()
d = temp[0:3]
k = temp[3]
if k == 1:
    d.sort()
else:
    d.sort(reverse=True)
print(' '.join(map(str,d)))
