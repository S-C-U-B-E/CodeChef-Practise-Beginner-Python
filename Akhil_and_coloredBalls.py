for _ in range(int(input())):
    X=input().upper()
    Y=input().upper()
    Z=""
    for i in range(len(X)):
        if X[i]=='B' and Y[i]=='B':
            Z+='W'
        else:
            Z+='B'
    print(Z)