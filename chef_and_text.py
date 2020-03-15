for _ in range(int(input())):
    n=int(input())
    s=list(input())
    #st=""
    for i in range(len(s)):
        #a-m n-z
        #0-4 5-9
        c=ord(s[i])
        if c>=97 and c<=109 or c>=65 and c<=77:
            s[i]=chr(c+13)

        elif c>=110 and c<=122 or c>=78 and c<=90:
            s[i]=chr(c-13)

        elif c>=48 and c<=52:
            s[i]=chr(c+5)

        elif c>=53 and c<=57:
            s[i]=chr(c-5)

        elif s[i]==' ':
            s[i]=' '
    for i in s:
        print(i,end="")
    print()
