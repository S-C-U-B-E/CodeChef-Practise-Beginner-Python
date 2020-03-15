for _ in range(int(input())):
    p=[]

    for i in range(3):
        p.append(list(map(int,input().split())))
    temp1,gd=[],0
    for i in range(2):
        for j in p:
            temp1 = p.copy()
            temp1.remove(j)
            c,eq=0,0
            for k in temp1:
                for q in range(3):
                    if j[q]>k[q]:
                        c+=1
                    elif j[q]==k[q] and eq<2:
                        c+=1
                        eq+=1
                eq=0
            if c==len(temp1)*3:
                p.remove(j)
                gd+=1
                break
    if gd==2:
        print("yes")
    else:
        print("no")