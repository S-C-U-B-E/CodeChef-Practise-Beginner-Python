for _ in range(int(input())):
    s=input().strip('0')
    if '1' in s:
        if '0' in s[s.index('1'):]:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")

