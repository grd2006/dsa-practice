#Reverse the given number
#reversed number is {reverse_n//10}

n=int(input())
reverse_n=0
while(n>0):
    reverse_n+=n%10
    reverse_n*=10
    n//=10
print(reverse_n//10)