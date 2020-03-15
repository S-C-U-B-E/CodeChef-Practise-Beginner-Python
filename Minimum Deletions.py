
from functools import reduce
from math import gcd as gandu
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    if 1 in a or reduce(gandu,a)==1:
        print(0)
    else:
        print(-1)
