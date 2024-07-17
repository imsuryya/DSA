# Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between
#  1 and N, where N is taken as input from the user.

#need to be done

# nums = [2, 7, 11, 15]  # Correct declaration of the list
# target = 9  # Correct declaration of the target

# Iterate through the list to find pairs that add up to the target
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         print(nums[j])
#          if nums[i] + nums[j] == target:
#              print(f"Pair found: {nums[i]} and {nums[j]} at indices {i} and {j}")

# nums = [2, 7, 11, 15]
# target = 9 
# l = 0
# r = 1

# while r<len(nums):
#     if nums[l] + nums[r] == target:
#         print([l,r])
#         break
#     r+=1
#     if r == len(nums):
#         l += 1
#         r = l + 1
#     if l == len(nums) - 1:
#         break 
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#                 l = 1
#                 r = 1
#                 while r<len(nums):
#                     if nums[r] != nums[r-1]:
#                         nums[l]=nums[r]
#                         r+=1
#                         l+=1
#                     else:
#                             r+=1
#                 return l   


# nums = [0,0,1,1,1,2,2,3,3,4]
# sortedList = set(nums)
# sortedList = list(sortedList)
# if len(sortedList) != len(nums):
#     k = len(nums) - len(sortedList)
#     print(k)

nums = [2,7,11,15]
target = 9
const = 0
while const<len(nums):
    value = target - const
    



