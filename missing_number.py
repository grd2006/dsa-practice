nums=list(map(int,input().split()))
if 0 not in nums:
    print("0")
else:
    for i in range(len(nums)+1):
        if i not in nums:
            print(i)
            break