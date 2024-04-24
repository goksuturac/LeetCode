class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            odd = self.middle(s, i, i)
            even = self.middle(s, i, i+1)
            result = max(odd, even, result, key=len)
        return result

    def middle(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -=1 ; r +=1
        return s[l+1 : r]