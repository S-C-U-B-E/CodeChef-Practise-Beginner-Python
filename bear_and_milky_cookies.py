"""for _ in range(int(input())):
    n=int(input())
    s=input()
    #print(''.join(list(reversed(s[-1:len(s)-7:-1]))))
    if ("milk" in s  or "cookie milk" in s) and ("cookie cookie" not in s) and ''.join(list(reversed(s[-1:len(s)-7:-1])))!="cookie" :
        print("YES")#shortest_code <3
    else:
        print("NO")#LOL"""
for x in range(int(input())):
    n = input()
    k = input()
    if ('cookie cookie' in k) or k[-6:]=="cookie":
        #print(k[-6:])
        print('NO')
    else:
        print('YES')
