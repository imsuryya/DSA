# Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between
#  1 and N, where N is taken as input from the user.

#need to be done

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
