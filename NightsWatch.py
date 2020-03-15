for _ in range(int(input())):
    n=int(input())
    l=input()
    s=list(l)
    c=0
    if '1' in l:
        i=0
        while i<(n-1):
           if s[i]=='0' and s[i+1]=='0' and s[i+2]=='0':
               c+=1
               s[i+1]='1'
           elif s[i] == '0' and s[i + 1] == '0' and s[i + 2] == '1':
               c+=1
               s[i]='1'
           elif s[i] == '1' and s[i + 1] == '0':
                   if i+2<len(s) and s[i + 2] == '0':
                        c+=1
                        s[i+2]='1'
           i+=2
           if i and i+1<len(s):
               if s[i]==s[i+1]=='1':
                    c-=1
                    i+=1
    else:
        if len(s)%2==0:
            c=len(s)//2
        else:
            c=(len(s)//2)+1
    print(c)

