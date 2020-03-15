for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    if 0 in a:
        print(1000*(a.count(0))+100*(n-a.index(0)))
    else:
        print(0)