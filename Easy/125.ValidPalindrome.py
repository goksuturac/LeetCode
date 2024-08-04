from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newest = ''.join(char.lower() for char in s if char.isalnum())
        return newest == newest[::-1]
result = Solution()
