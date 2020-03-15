"""n=int(input())
for _ in range(n):
    st=input()
    if st.count('1')==0:
        print("Beginner")
    if st.count('1')==1:
        print("Junior Developer")
    if st.count('1')==2:
        print("Middle Developer")
    if st.count('1')==3:
        print("Senior Developer")
    if st.count('1')==4:
        print("Hacker")
    if st.count('1')==5:
        print("Jeff Dean")"""
from sys import stdin
mydict={0:"Beginner",1:"Junior Developer",2:"Middle Developer",3:"Senior Developer",4:"Hacker",5:"Jeff Dean"}
t=int(stdin.readline())
while t>0:
    A=list(map(int , stdin.readline().split()))
    s=sum(A)
    print(s)
    print(mydict[s])
    t=t-1
