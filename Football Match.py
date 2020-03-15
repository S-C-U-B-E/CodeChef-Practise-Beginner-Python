for _ in range(int(input())):
    n=int(input())
    lo=[]
    for _ in range(n):
        lo.append(input())
    s = list(set(lo))
    if n==0:
        print("Draw")
    elif len(s)==1:
        print(s[0])
    else:
        t1=lo.count(s[0])
        t2=lo.count(s[1])
        if t1>t2:
           print(s[0])
        elif t2>t1:
           print(s[1])
        else:
            print("Draw")