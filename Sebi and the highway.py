for _ in range(int(input())):
    s,sg,fg,d,t=map(int,input().split())
    kph=(d*50*18)/(t*5)
    print(kph)
    print((18/5)*((d*50)/t))
    stot=s+kph
    sebidiff=abs(sg-stot)
    fatherdiff=abs(fg-stot)
    if fatherdiff<sebidiff:
        print("FATHER")
    elif sebidiff<fatherdiff:
        print("SEBI")
    else:
        print("DRAW")

