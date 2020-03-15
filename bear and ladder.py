for _ in range(int(input())):
    a,b=[int(x) for x in input().split()]
    if abs(b - a) == 1 and min(a,b)%2==1:
        print("YES")
    elif abs(b - a) == 2:
            print("YES")
    else:
        print("NO")

