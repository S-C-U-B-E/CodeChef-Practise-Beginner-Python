x=0
t=int(input())
while t!=0:
    s=input()
    s+=" "
    st = ""
    c=0
    for i in s:
        if i!=' ':
            st+=i
        else:
            if st=="not":
                print("Real Fancy")
                c+=1
                break
            st=""
    if c==0:
        print("regularly fancy")
    t-=1











