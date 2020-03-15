for _ in range(int(input())):
    a,t=[],0
    for i in range(10):
        a.append([int(x) for x in input().split()])
    for i in range(10):
        for j in range(10):
            if a[i][j]<=30:
                t+=1
    if t>=60:
        print("yes")
    else:
        print('no')