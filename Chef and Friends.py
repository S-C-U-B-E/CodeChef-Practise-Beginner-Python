n=int(input())
count=0
for _ in range(n):
    u=input().lower()
    s=['ch','ef','he']
    for i in s:
        if i in u:
            count+=1
            break
print(count)
