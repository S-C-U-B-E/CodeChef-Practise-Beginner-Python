t=int(input())
while t!=0:
    c=0
    x=input().strip().split()
    for i in x:
        if i=="not":
            print("Real Fancy")
            c+=1
            break
    if c==0:
        print("regularly fancy")
    t-=1