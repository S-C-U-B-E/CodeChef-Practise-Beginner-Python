for _ in range(int(input())):
    s=input()
    n=len(s)
    g=['AB','BA']
    if  n%2==0 and all(s[i:i+2] in g for i in range(0,len(s)-1,2)):
        print("yes")
    else:
        print("no")