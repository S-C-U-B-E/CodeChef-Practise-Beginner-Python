for _ in range(int(input())):
    s =input()
    s+=" "
    s=list(s)
    sc=mc=0
    for i in range(len(s)):
        if s[i]=='s':
            if s[i+1]!='m':
                sc+=1
            else:
                mc+=1
                s[i+1]='*'
        if s[i]=='m':
            mc+=1
            if s[i+1]=='s':
                s[i+1]='*'
    if mc==sc:
        print("tie")
    elif mc>sc:
        print("mongooses")
    else:
        print("snakes")#hissss

