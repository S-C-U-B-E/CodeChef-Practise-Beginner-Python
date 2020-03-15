dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
s=input()
ini,fin=0,0
x=0
t=[]
for i in s:
    t.append(dict[i])
maxy=max(t)
base=maxy+1
te=len(t)-1
'print(t,maxy,base,te)'
for i in t:
    fin += i * (base ** te)
    te = te - 1


'print(fin)'

while True:
    """x+=1
    print()
    print(x)"""

    ini=fin
    t1=list(str(fin))
    fin = 0

    maxy = int(max(t1))
    base = maxy + 1
    te = len(t1) - 1

    'print(t1,maxy,base,te)'

    for i in t1:
        fin += int(i) * (base ** te)
        te = te - 1
        'print(fin)'

    'print(fin)'
    if fin==ini:
        break
print(fin)

