for _ in range(int(input())):
    r,c,k=map(int,input().split())
    s=0

    one=k
    r1=r
    r1 -= 1
    while one>0 and r1>0:
        r1-=1
        if ((r1-r)**2)+((c-c)**2) <= 2:
            s+=1
        else:
            break
        one-=1

    print("s one: "+str(s))
    s2=0

    two = k
    r1 = r
    r1 += 1
    while two > 0 and r1 < 9:
        r1 += 1
        if ((r1 - r) ** 2) + ((c - c) ** 2) <= 2:
            s += 1
            s2+=1
        else:
            break
        two-=1

    print("s two: " + str(s2))
    s3=0

    three = k
    c1 = c
    c1 -= 1
    while three > 0 and c1 > 0:
        c1 -= 1
        if ((r - r) ** 2) + ((c1 - c) ** 2) <= 2:
            s += 1
            s3+=1
        else:
            break
        three-=1

    print("s three: " + str(s3))
    s4=0

    four = k
    c1 = c
    c1 += 1
    while four > 0 and c1 < 9:
        c1 += 1
        if ((r - r) ** 2) + ((c1 - c) ** 2) <= 2:
            s += 1
            s4+=1
        else:
            break
        four-=1

    print("s four: " + str(s4))
    s5=0

    five = k
    r1 = r
    c1=c
    r1 -= 1
    c1 -= 1
    while five > 0 and r1 > 0 and c1 >0:
        r1 -= 1
        c1-=1
        if ((r1 - r) ** 2) + ((c1 - c) ** 2) <= 2:
            s += 1
            s5+=1
        else:
            break
        five-=1

    print("s five: " + str(s5))
    s6=0

    six = k
    r1 = r
    c1=c
    r1 += 1
    c1 += 1
    while six > 0 and r1 < 9 and c1 < 9:
        r1 += 1
        c1+=1
        if ((r1 - r) ** 2) + ((c1 - c) ** 2) <= 2:
            s += 1
            s6+=1
        else:
            break
        six-=1

    print("s six: " + str(s6))
    s7=0

    seven = k
    r1 = r
    c1=c
    r1 -= 1
    c1 += 1
    while seven > 0 and r1 > 0 and c1 < 9:
        r1 -= 1
        c1+=1
        if ((r1 - r) ** 2) + ((c1 - c) ** 2) <= 2:
            s += 1
            s7+=1
        else:
            break
        seven-=1

    print("s seven: " + str(s7))
    s8=0

    eight = k
    r1 = r
    c1=c
    r1 += 1
    c1 -= 1
    while eight > 0 and r1 < 9 and c1 > 0:
        r1 += 1
        c1-=1
        if ((r1 - r) ** 2) + ((c1 - c) ** 2) <= 2:
            s += 1
            s8+=1
        else:
            break
        eight-=1

    print("s eight: " + str(s8))

    s+=1
    print(s)