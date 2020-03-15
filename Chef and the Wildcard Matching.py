for _ in range(int(input())):
    x,y=input(),input()
    flag=1
    for i in range(len(x)):
        if x[i]!='?' and y[i]!='?':
            if x[i]!=y[i]:
                print("No")
                flag=0
                break
    if flag:
        print("Yes")

