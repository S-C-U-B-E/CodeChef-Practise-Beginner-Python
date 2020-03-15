"""s=input().upper()
cont=0
if 'C' in s:
    c=s.index('C')
    while c<len(s):
        if 'C' in s[c:]:
            c=s.index('C')
            s=s.replace('C',' ',1)
            if 'H' in s[c:]:
                s=s.replace('H', ' ', 1)
                if 'E' in s[c:]:
                    s=s.replace('E', ' ', 1)
                    if 'F' in s[c:]:
                        s=s.replace('F', ' ', 1)
                        cont+=1
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break
print(cont)
#CHEFCHEFFFF
#PHHHEEEFFCC"""
s=input().lower()
count=0
c,h,e,f=0,0,0,0
for i in s:
    if i=='c':
        c+=1
    if i=='h' and c>0:
        if c>h:h+=1
    if i=='e' and h>0:
        if h>e:e+=1
    if i=='f' and e>0:
        if e>f:f+=1
print(min(c,h,e,f))