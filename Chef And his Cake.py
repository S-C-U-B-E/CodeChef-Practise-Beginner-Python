for _ in range(int(input())):
    n,m=map(int,input().split())
    red,green=0,0
    for i in range(n):
        s=input()
        if i%2==0:
            for l in range(m):
                if l%2==0 and s[l]=='R':
                    green+=5
                elif l%2!=0 and s[l]=='G':
                    green+=3

                if l%2==0 and s[l]=='G':
                    red+=3
                elif l%2!=0 and s[l]=='R':
                    red+=5
        elif i%2!=0:
            for l in range(m):
                if l%2==0 and s[l]=='G':
                    green+=3
                elif l%2!=0 and s[l]=='R':
                    green+=5

                if l%2==0 and s[l]=='R':
                    red+=5
                elif l%2!=0 and s[l]=='G':
                    red+=3

    if red<green:
        print(red)
    else:
        print(green)