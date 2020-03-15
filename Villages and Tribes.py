for _ in range(int(input())):
    s=input()
    fa,fb,ca,cb=None,None,0,0
    for i in range(len(s)):
        if s[i]=='A':
            if fa is not None:
                ca+=i-fa
            else:
                ca+=1
            fa = i
            fb=None
        if s[i] == 'B':
            if fb is not None:
                cb += i - fb
            else:
                cb += 1
            fb = i
            fa = None

    print(ca,cb)