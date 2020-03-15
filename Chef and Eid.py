import sys
for _ in range(int(input())):
    n=int(input())
    v=[int(x) for x in input().split()]
    v.sort()
    mini=sys.maxsize
    for i in range(n-1):
        if abs(v[i]-v[i+1])<mini:
            mini=abs(v[i]-v[i+1])
    print(mini)