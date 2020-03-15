_=int(input())
a=[0 if int(x)%2==0 else 1 for x in input().split()]
print("READY FOR BATTLE"*bool(a.count(0)>a.count(1))+"NOT READY"*bool(a.count(0)<=a.count(1)))