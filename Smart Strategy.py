import numpy as np
for _ in range(int(input())):
    n,q=map(int,input().split())
    d=[int(x) for x in input().split()]
    x=[int(x) for x in input().split()]
    mul=np.prod(d)
    for i in x:
        print(str(i//mul),end=' ')
    print()