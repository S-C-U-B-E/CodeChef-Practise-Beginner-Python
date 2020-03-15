for _ in range(int(input())):
    s=input()
    for i in s:
        if not i.isalpha():
            s=s.replace(i,'',1)
    s.lower()
    cll=['chef', 'chfe', 'cehf', 'cefh', 'cfeh', 'cfhe', 'hcef', 'hcfe', 'hecf', 'hefc', 'hfec', 'hfce', 'ehcf', 'ehfc', 'echf', 'ecfh', 'efch', 'efhc', 'fhec', 'fhce', 'fehc', 'fech', 'fceh', 'fche']
    c=0
    for i in range(len(s)-3):
        if s[i:i+4] in cll:
            c+=1
    if c:
        print("lovely",c)
    else:
        print("normal")