# Final 

nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i):
        if(nums[i]+nums[j]==target):
            print(j,i)
        else:
            continue;