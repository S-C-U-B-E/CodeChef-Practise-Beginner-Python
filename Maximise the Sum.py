for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    su=0
    for i in range(n//2):
        su+=abs(a[n-(i+1)]-a[i])
    print(su)