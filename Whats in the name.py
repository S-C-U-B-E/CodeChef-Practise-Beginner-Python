for _ in range(int(input())):
    s=list(input().lower().split(' '))
    st=""
    for i in range(len(s)-1):
        st+=s[i][0].upper()+". "
    print(st+s[len(s)-1].capitalize())