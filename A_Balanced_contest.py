for _ in range(int(input())):
    p2=p10=0
    n,p=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    for i in a:
        if i>=(p//2):
            p2+=1
        elif i<=(p//10):
            p10+=1
    if p2==1 and p10==2:
        print("yes")
    else:
        print("no")
#what the ****