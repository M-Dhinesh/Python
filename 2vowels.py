lst=list(input().split())
for i in lst:
    count=0
    for x in i:
        if "a" in x or "e" in x or "i" in x or "o" in x or "u" in x:
            count=count +1
    if count>=2:
        print(i)
        continue