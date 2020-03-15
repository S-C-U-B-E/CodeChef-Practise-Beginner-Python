for _ in range(int(input())):
    c,d,l=map(int,input().split())
    if l%4==0 :
        ma=c*4+d*4
        if d*2>=c:
            mi=d*4
        else:
            mi=(c-(d*2))*4+d*4
        if l in range(mi,ma+1):
            print("yes")
            continue
    print("no")