n=int(input())
prime, composite=0, 0
while(n>0):
    if n%10==2 or n%10==3 or n%10==5 or n%10==7:
        prime+=1
    elif n%10==0 or n%10==4 or n%10==6 or n%10==8 or n%10==9:
        composite+=1
    n//=10
print(prime)
print(composite)

