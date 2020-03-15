for _ in range(int(input())):
    n=int(input())
    s=set([int(x) for x in input().split()])
    m=int(input())
    f=set([int(x) for x in input().split()])
    print("Yes" if len(s.intersection(f))==len(f) else "No")