# At ITM University, every student is assigned a unique numeric activity, students are asked to calculate the sum of all digits present in their student ID.
# Given an integer N representing the student ID, find the sum of its digits.

n=int(input())
sum=0
while(n>0):
    sum+=n%10
    n//=10
print(sum)