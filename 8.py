# Q2. Count Even and Odd Digits
# Problem
# Given a positive integer N, count how many even digits and odd digits are present in the number.
# Example
# Input
# 123456
# Output
# Even: 3
# Odd: 3

n=int(input())
even=0
odd=0
while n>0:
    if n%2==0:
        even+=1
    elif n%2!=0:
        odd+=1
    n//=10
print(f"Even: {even}")
print(f"Odd: {odd}")

