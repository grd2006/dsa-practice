# palindrome
# 001100 edge test case solved using string because integer input doesn't store the starting two 0's since they have no value

n=input()
reverse_n=""
i=(len(n)-1)
while(i>=0):
    reverse_n+=n[i]
    print(n[i])
    i-=1
if n==reverse_n:
    print(True)
else:
    print(False)
