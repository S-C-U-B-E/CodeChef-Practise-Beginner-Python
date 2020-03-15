for _ in range(int(input())):
    a=[int(x) for x in input().split()]
    s=list(set(a))
    if (len(s)==2 and a.count(s[0])==2 and a.count(s[1])==2) or (len(s)==1):print("YES")
    else:print("NO")
