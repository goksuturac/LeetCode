from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        C = nums1 + nums2
        C.sort()

        if len(C) % 2 == 0:
            median1_index = len(C) // 2 - 1
            median1 = C[median1_index]
            median2 = C[median1_index+1]
            median = (median1 + median2) / 2
            return median
        else:
            median_index = len(C) // 2
            median = C[median_index]
            return median
