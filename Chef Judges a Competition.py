for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    a.sort()
    b.sort()
    asu=sum(a[0:n-1])
    bsu=sum(b[0:n-1])
    if asu<bsu:
        print("Alice")
    elif bsu<asu:
        print("Bob")
    else:
        print("Draw")
