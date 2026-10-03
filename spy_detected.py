t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    if a[0]!=a[1]:
        if a[1]==a[2]:
            print("1")
        elif a[0]==a[2]:
            print("2")
    elif a[0]==a[1]:
        for j in range(2, n):
            if a[0]!=a[j]:
                print(j+1)
                break