t=int(input())
for i in range(t):
    n=int(input())
    count=0
    power=0
    list1=[]
    while (n>0):
        if n%10!=0:
            list1.append((n%10)*(10**power))
            count+=1
        power+=1
        n//=10
    print(count)
    z=0
    while(z<len(list1)):
        print(list1[z], end=" ")
        z+=1