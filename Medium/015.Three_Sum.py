from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return([])
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
# solution 1:
        # for i in range(0, len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             if (nums[i] + nums[j] + nums[k] == 0):
        #                 result.append(tuple(sorted([nums[i], nums[j], nums[k]])))
        # return list(set(result))
# solution 2:
        nums = sorted(nums)
        for i in range(0, len(nums)-2):
            lower = i + 1
            upper = len(nums) - 1
            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]
                if s == 0:
                    result.append((nums[i], nums[lower], nums[upper]))
                    lower += 1
                elif s < 0:
                    lower += 1
                else:
                    upper -= 1
        return list(set(result))            