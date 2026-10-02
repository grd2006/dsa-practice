# During a coding training program at ITM University, a student practices coding for N days. On day i, the student solves A[i] coding problems.
# A day is called an Improvement Day if the student solves at least 3 more problems than the previous day.
# The first day is never considered an Improvement Day.
# Find the total number of Improvement Days.
# Input
# 7
# 2 5 6 10 9 15 17
# Output
# 3
# Explanation
# Compare each day with the previous day:
# Day 2: 5 - 2 = 3 → Improvement Day
# Day 3: 6 - 5 = 1 → Not an Improvement Day
# Day 4: 10 - 6 = 4 → Improvement Day
# Day 5: 9 - 10 = -1 → Not an Improvement Day
# Day 6: 15 - 9 = 6 → Improvement Day
# Day 7: 17 - 15 = 2 → Not an Improvement Day
# Therefore, the total number of Improvement Days = 3.

n=int(input())
list2=list(map(int, input().split()))
improvement_days= 0

for i in range(n-1):
    if (list2[i]+3)<=list2[i+1]:
        improvement_days+=1
print(improvement_days)