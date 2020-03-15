for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    s=set(a)
    if (2 not in s) and (5 in s):
       if sum(a)/n>=4.0:print("Yes")
       else:print("No")
    else:print("No")
