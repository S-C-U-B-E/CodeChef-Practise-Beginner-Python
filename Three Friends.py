for _ in range(int(input())):
    x,y,z=map(int,input().split())
    sets=[[-x,y,z],[x,-y,z],[x,y,-z]]
    c=0
    for i in sets:
       if abs(i[0]+i[1])==abs(i[2]) and abs(i[1]+i[2])==abs(i[0]) and abs(i[0]+i[2])==abs(i[1]):
           c+=1
           break
    if c:
        print("yes")
    else:
        print("no")