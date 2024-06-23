from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        combination = []

        def kSum(k,start, target):
            if k != 2:
                for i in range(start, len(nums)-k + 1):
                    #art arda iki sayı da aynıysa sonuçta duplicate olacak o yüzden continue
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    combination.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    combination.pop()
                return
            
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    result.append(combination + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum(4,0,target)
        return result