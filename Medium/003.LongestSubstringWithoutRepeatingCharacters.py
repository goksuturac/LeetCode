class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current, distance, start = 0,0,0
        N = len(s)
        i = 0
        check = {}

        while i < N:
            if s[i] not in check:
                current+=1
            else:
                start = max(start, check[s[i]])
                current = i- start
            check[s[i]] = i
            distance = max(current, distance)
        return distance