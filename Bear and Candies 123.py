for _ in range(int(input())):
    a,b=map(int,input().split())
    li,bo,c=0,0,0
    while li<=a and bo<=b:
        c+=1
        li+=c
        c+=1
        bo+=c
    if li > a:
        print("Bob")
    elif bo > b:
        print("Limak")