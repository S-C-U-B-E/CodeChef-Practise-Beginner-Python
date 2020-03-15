for _ in range(int(input())):
    n=int(input())
    b=list(range(1,n+1))
    #print(b)
    for i in range(n-1,0,-1):
        #print(b[i],end="**")
        if not b[i]&(b[i]-1):
            print(b[i])
            break
        else:
            continue
