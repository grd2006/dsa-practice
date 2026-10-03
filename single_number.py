nums=list(map(int, input().split()))
nums.sort()
if len(nums)==1:
    print(nums[0])
elif nums[len(nums)-1]!=nums[len(nums)-2]:
    print(nums[len(nums)-1])
else:
    for i in range(0, len(nums)-1, 2):
        if nums[i]!=nums[i+1]:
            print(nums[i])
            break