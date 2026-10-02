# Q3. Find the Largest Digit
# Problem
# Given a positive integer N, find the largest digit present in the number.
# Example
# Input
# 58329
# Output
# 9

n=int(input())
maximum=0
while (n>0):
    if n%10>maximum:
        maximum=n%10
    n//=10
print(maximum)