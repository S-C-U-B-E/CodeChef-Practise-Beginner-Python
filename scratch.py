a="12345678"
b=[]
st=""
l=len(a)
lim=-1
print(l)
for i in range(l):
    lim=i
    print("\n\n"+str(i+1)+"\n")
    print(str(a[i]))
    if a[i] not in b:
        b.append(str(a[i]))
    while lim<l-1:
        #print()
        #st=""
        lim+=1
        for j in range(lim,l):
            print(str(a[i]),end=" ")
            st=st+str(a[i])
            for k in range(lim,j+1):
                st = st + str(a[k])
                print(str(a[k]),end=" ")
            print()
            if st not in b:
                b.append(st)
            st=""
print(b)

if "67" in b:
    print("<<<<<<<<IT IS THERE>>>>>>>>>")
else:
    print("<<<<<<<<IT IS NOT THERE>>>>>>>>>")