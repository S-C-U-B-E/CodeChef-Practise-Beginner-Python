for _ in range(int(input())):
    s1,s2=input(),input()
    mind,minx=0,0
    for i in range(len(s1)):
        if s1[i]!='?' and s2[i]!='?':
            if s1[i]!=s2[i]:
                mind+=1
    for i in range(len(s1)):
        if s1[i]=='?' or  s2[i]=='?':
            minx+=1
    print(mind,minx+mind)