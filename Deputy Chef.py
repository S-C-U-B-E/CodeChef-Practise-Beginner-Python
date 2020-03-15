for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    d=[int(x) for x in input().split()]
    s=-1
    for i in range(n):
        if i==0:
            if d[i]>a[1]+a[-1]:
                if d[i]>s:
                    s=d[i]
        elif i==n-1:
            if d[i]>a[0]+a[-2]:
                if d[i]>s:
                    s=d[i]
        elif d[i]>a[i-1]+a[i+1]:
            if d[i] > s:
                s = d[i]
    print(s)