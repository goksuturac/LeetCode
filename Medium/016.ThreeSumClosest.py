from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 0
        best_result = 100000
        nums.sort()

        for i in range(0, len(nums)-2):
            if nums[i] == nums[i-1] and i > 0:
                continue

            lower = i + 1
            upper = len(nums) - 1

            while lower < upper:
                result = nums[i] + nums[lower] + nums[upper]

                if result == target:
                    return result

                if abs(target-result) < abs(target - best_result):
                    best_result = result
                    
                if result <= target:
                    lower += 1
                    while(nums[lower] == nums[lower-1] and lower < upper):
                        lower += 1
                else:
                    upper -= 1
        return best_result  
        