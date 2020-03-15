for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    s=0
    for i in a:
        s^=(2*i)
    print(s)