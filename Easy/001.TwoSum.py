from typing import List

# # Solution 1:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return([i, j]) 

# Solution 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, num in enumerate(nums):
            if target - num in checked:
                return([checked[target - num], i])
            elif num not in checked:
                checked[num] = i