for _ in range(int(input())):
    s=input().upper()
    dc=uc=-1
    U=D=0
    for i in s:
        if i=='U' and uc==-1:
            U+=1
            dc=-1
            uc=0
        if i=='D' and dc==-1:
            D+=1
            uc=-1
            dc=0
    if U<=D:
        print(U)
    else:
        print(D)