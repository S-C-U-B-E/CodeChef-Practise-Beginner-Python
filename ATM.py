x,y=input().split()
x=int(x)
y=float(y)

if x%5==0:
    if y-x-0.5>=0:
        y-=(0.5+x)
y="{0:.2f}".format(y)
print(y)
