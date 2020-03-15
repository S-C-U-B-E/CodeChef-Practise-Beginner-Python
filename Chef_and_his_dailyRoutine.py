for _ in range(int(input())):
    st=input().upper()
    strin=sorted(st)
    print(strin)
    c=e=s=1
    tot=0
    for i in st:
        if i=='C' and c==1:
            tot+=c
        if i=='E' and e==1:
            c=0
            tot+=e
        if i=='S' and s==1:
            e=0
            c=0
            tot+=s
    if tot==len(st):
        print("yes")
    else:
        print("no")