for _ in range(int(input())):
    s=input()
    if s.count('01')+s.count('10')+int(s[0]!=s[len(s)-1])<=2:
        print("uniform")
    else:
        print("non-uniform")