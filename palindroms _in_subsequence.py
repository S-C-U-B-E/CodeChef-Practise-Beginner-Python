s="SHANKHASHUBHRASAN"
l=len(s)
index=[]
sub_seq=[]
pals=[]

def pal(st):
    l=len(st)
    for i in range(int(l/2)):
        #print(st[i])
        #print(st[-(i+1)])
        if st[i]!=st[-(i+1)]:
            return 0
    return 1

def formation(s_val ,val_ind):
    for j in range(val_ind+1,l):
        if [j]>index:
            st=s_val+s[j]
            index.append(j)
            if st in sub_seq or st==s:
                return
            else:
                sub_seq.append(st)
                if pal(st):
                    pals.append(st)
                formation(st,j)

for i in range(l):
    index.clear()
    index.append(i)
    sub_seq.append(s[i])
    formation(s[i],i)

sub_seq.append(s)

"""for v in range(len(sub_seq)):
    print("SENT: " + str(sub_seq[v]), end="......")
    t = pal(str(sub_seq[v]))
    if t:
        pals.append(sub_seq[v])
        print("PALINDROM")
    else:
        print("NON_PALINDROM")"""

print("\n\n<<<<<<<<HENCE, PALINDROMS>>>>>>>>")
for i in pals:
    print(i,end=" ")