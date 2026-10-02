# Question 1: Lucky Digit Counter
# Rohan enters a positive integer N. Count how many digits in the number are equal to 7.
# Input
# 274757
# Output
# 3

n=int(input())
count=0
while n>0:
    if n%10==7:
        count+=1
    n//=10
print(count)