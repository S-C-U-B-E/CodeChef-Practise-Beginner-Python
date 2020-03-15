for _ in range(int(input())):
    a=[int(x) for x in input().split()]
    c,flag=0,1
    for i in a:
        if i==1:
            c+=1
            if c>5:
                flag=0
                break
        else:
            c=0
    if flag:
        print("#allcodersarefun")
    else:print("#coderlifematters")