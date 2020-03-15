for _ in range(int(input())):
    n=int(input())
    ci1, di1 = 0, 0
    ci2, di2 = 0, 0
    ci3, di3 = 0, 0
    for i in range(n):
        c,l,x=map(int,input().split())
        if l==1:
            if x>di1:
                di1=x
                ci1=c
            elif x==di1:
                if c<ci1:
                    ci1=c
        elif l==2:
            if x>di2:
                di2=x
                ci2=c
            elif x==di2:
                if c<ci2:
                    ci2=c
        elif l==3:
            if x>di3:
                di3=x
                ci3=c
            elif x==di3:
                if c<ci3:
                    ci3=c
    print(di1,ci1)
    print(di2, ci2)
    print(di3, ci3)