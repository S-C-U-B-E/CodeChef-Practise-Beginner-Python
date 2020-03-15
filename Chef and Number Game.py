for _ in range(int(input())):
    n=int(input())
    a=[1 if int(x)>0 else 0 for x in input().split()]
    #print(*a)
    pos,neg=a.count(1),a.count(0)
    if pos==0:
        print(neg,neg)
    elif neg==0:
        print(pos,pos)
    elif pos>neg:
        print(pos,neg)
    else:
        print(neg,pos)
