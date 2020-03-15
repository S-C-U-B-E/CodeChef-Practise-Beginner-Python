for _ in range(int(input())):
    n,k=map(int,input().split())
    h=[int(x) for x in input().split()]
    hf,c=0,0
    for i in h:
        if i-hf>k:
            c+=(i-hf-1)//k
        hf=i
    print(c)