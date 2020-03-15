for _ in range(int(input())):
    n=int(input())
    loss=0
    for i in range(n):
        p,q,d=map(int,input().split())
        sp=p+(p*d)/100
        sp-=(sp*d)/100
        if sp<p:
            loss+=(p-sp)*q
    print("{:.9f}".format(loss))