a, b = map(int, input().split())
count=0
if 1<=a<=b<=10:
    while a<=b:
        a*=3
        b*=2
        count+=1
print(count)
