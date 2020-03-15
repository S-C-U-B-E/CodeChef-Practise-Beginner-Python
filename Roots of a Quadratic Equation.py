from math import sqrt
a,b,c =int(input()),int(input()),int(input())
x1=(-b+sqrt(pow(b,2)-(4*a*c)))/(2*a)
x2=(-b-sqrt(pow(b,2)-(4*a*c)))/(2*a)
print(x1)
print(x2)