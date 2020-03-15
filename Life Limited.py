for _ in range(int(input())):
    a,f=[],0
    for _ in range(3):
        a.append(list(input()))
    for i in range(2):
        if not f:
            for j in range(2):
                if a[i][j]=='l' and a[i+1][j]=='l' and a[i+1][j+1]=='l':
                    print('yes')
                    f=1
                    break
    if f!=1:
        print('no')