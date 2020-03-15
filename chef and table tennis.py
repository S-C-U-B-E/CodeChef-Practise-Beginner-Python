for _ in range(int(input())):
    s=input()
    ls=0
    wn=0
    c=True
    for i in range(len(s)):
        if not int(s[i]):
            ls+=1
        if int(s[i]):
            wn+=1
        if ls == wn == 10:
           c=False
           for j in range(i+1,len(s)):
               if not int(s[j]):
                   ls+=1
               if int(s[j]):
                   wn+=1
               if (ls-wn)==2:
                   print("LOSE")
               elif (wn-ls)==2:
                   print("WIN")

        if (ls==11 or wn==11) and c:
            print("LOSE"*bool(ls==11)+"WIN"*bool(wn==11))
            break
