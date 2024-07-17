nums = [2,7,11,15]
target = 9
for i in range(0,len(nums)):
    value = target - nums[i]
    if value != nums[i]:
        i+=1
    else:
        print([value,i])    