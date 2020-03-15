'''l=float(input())
b=float(input())
p=2*(l+b)
a=l*b
if a>p:
    print("Area")
    print(int(a))
elif a<p:
    print("Peri")
    print(int(p))
else:
    print("Eq")
    print(int(a))'''
a, b=int(input()), int(input())
a, b=a*b, 2*(a+b)
print("Area"*(a>b)+"Peri"*(b>a)+"Eq"*(b==a),a+(b>a)*(b-a),sep='\n')