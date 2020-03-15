import math as aaa
import sys
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    mini=sys.maxsize
    for i in range(n-1):
        for j in range(i+1,n):
            if (a[i]*a[j])//aaa.gcd(a[i],a[j])<mini:
                mini=(a[i]*a[j])//aaa.gcd(a[i],a[j])
    print(mini)