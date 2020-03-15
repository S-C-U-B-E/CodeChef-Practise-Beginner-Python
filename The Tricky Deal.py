from math import pow
for _ in range(int(input())):
    a=int(input())
    i,s,chs,pr=1,0,0,0
    d1,d2=0,0
    while True:
      s+=a
      ch=pow(2,i-1)
      chs+=ch
      if chs>s:
          break
      else:
          d1=i
      if a-ch>0:
        d2=i
      i+=1
    print(d1,d2)


