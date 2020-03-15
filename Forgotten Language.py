for _ in range(int(input())):
     n,k=map(int,input().split())
     mydik={}
     for x in input().split():
         mydik.setdefault(x, 0)
     #print(mydik)
     for _ in range(k):
         s=input()
         for i in mydik:
             if i in s:
                 mydik[i]+=1
     #print(mydik)
     for i in mydik:
         print("YES"*bool(mydik[i]>0)+"NO"*bool(mydik[i]==0),end=' ')
     print()