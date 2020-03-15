#e=2.71828
"""print("---------                     ")
print("|            |           |         /\\          |\\        |  |    /   |          |         /\\")
print("|            |           |        /  \\         |  \\      |  |   /    |          |        /  \\")
print("|            |           |       /    \\        |   \\     |  |  /     |          |       /    \\")
print("---------    |___________|      /      \\       |    \\    |  | /      |__________|      /      \\")
print("         |   |           |     /________\\      |     \\   |  |/       |          |     /________\\")
print("         |   |           |    /          \\     |      \\  |  | \\     |          |    /          \\")
print("         |   |           |   /            \\    |       \\ |  |  \\    |          |   /            \\")
print("---------    |           |  /              \\   |        \\|  |   \\   |          |  /              \\")

print("\n\n")

print(2%1)
print(4%1)
print(6%1)
u=8
f=[]
for _ in range(u):
    f.append([])
f[1].append(4)
print(f)
for i in range(1,5):
    f[i-1].append(i)
print(f)"""

x=40
y=35
z=20
w=10

#BODMAS RULE:

print("y/z: "+str(y/z)) # AAGE DIVISION
print("x*y/z: "+str(x*y/z)) #THEN MULTIPLICATION
print("x*y/z-w: "+str(x*y/z-w))  # LAST SUBSTRACTION
print("RESULT: "+str(x*y/z-w))  # RESULT

print()

print("z-w: "+str(z-w)) # AAGE BRACKET
print("y/(z-w): "+str(y/(z-w))) #THEN DIVIDE
print("x*y/(z-w): "+str(x*y/(z-w))) #THEN MULTI.
print("RESULT: "+str(x*y/(z-w))) #RESULT

print("DIFFERENCE:  "+str( (x*y/(z-w) - (x*y/z-w)  )))