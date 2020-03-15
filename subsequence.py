import time
start=time.time()
s="1073741824"
l=len(s)
index=[]
sub_seq=[]

def pal(st):
    le=len(st)
    for j in range(int(le/2)):
        #print(st[j])
        #print(st[-(j+1)])
        if st[j]!=st[-(j+1)]:
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
                formation(st,j)


for i in range(l):
    index.clear()
    index.append(i)
    sub_seq.append(s[i])
    formation(s[i],i)

sub_seq.append(s)
print(sub_seq)

print("\n<<<<ALL PALINDROMS>>>>")
for i in sub_seq:
    t=pal(i)
    if t:
        print(i)
end=time.time()
print(end-start)