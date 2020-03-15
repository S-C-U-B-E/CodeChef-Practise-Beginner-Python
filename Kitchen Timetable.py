for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    d,s=0,0
    a.insert(0,d)
    for i in range(1,n+1):
        if a[i]-a[i-1]>=b[i-1]:
            s+=1
    print(s)