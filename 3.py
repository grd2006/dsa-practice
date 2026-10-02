# 3. Lucky Practice Day – ITM University
# During a coding training program at ITM University, a student practices coding for N days. On day i, the student solves A[i] coding problems.
# A day is called a Lucky Practice Day if:
# The student solves at least 5 problems, and
# The number of problems solved is divisible by 3 or 5.
# Find the total number of Lucky Practice Days.
# Input
# 8
# 3 5 6 7 9 10 11 15
# Output
# 5
# Explanation
# Check each day:
# 3 → Less than 5 → Not Lucky
# 5 → Divisible by 5 → Lucky
# 6 → Divisible by 3 → Lucky
# 7 → Not divisible by 3 or 5 → Not Lucky
# 9 → Divisible by 3 → Lucky
# 10 → Divisible by 5 → Lucky
# 11 → Not divisible by 3 or 5 → Not Lucky
# 15 → Divisible by both 3 and 5 → Lucky
# Therefore, the total number of Lucky Practice Days = 5.

n=int(input())
a=list(map(int, input().split()))
x=0

for i in range(n):
    if a[i]>=5 and (a[i]%3==0 or a[i]%5==0):
        x+=1
print(x)