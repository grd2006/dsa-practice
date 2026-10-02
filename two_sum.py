nums=list(map(int, input().split()))
target=int(input())
total=0
i=0
temp_i=0
indexes=[]
while(total<target):
    indexes.append(i)
    total+=nums[i]
    i+=1
    if total==target:
        print(indexes)
    elif total>target:
        total=0
        indexes=[]
        temp_i+=1
        i=temp_i

 