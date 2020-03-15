t=list(map(int,input().strip().split()))
while t[0]!=0:
    x=input().strip().split()
    if "not" in x:
        print("Real Fancy")
    else:
        print("regularly fancy")
    t[0]-=1