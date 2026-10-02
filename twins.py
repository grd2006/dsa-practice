n=int(input())
if 1<=n<=100:
    a=list(map(int, input().split()))
    a.sort()
    total=sum(a)
    count=0
    temp=0
    i=len(a)-1
    while(temp<=total/2):
        temp+=a[i]
        i-=1
        count+=1
    print(count)