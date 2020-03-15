for _ in range(int(input())):
    s=input()
    if 'a' and 'b' in s:
        if s.count('a')>s.count('b'):
            print(s.count('b'))
        else:
            print(s.count('a'))
    else:
        print(0)