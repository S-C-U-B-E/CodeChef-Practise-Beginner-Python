for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    a.sort()
    print(a[abs((n+k)//2)])