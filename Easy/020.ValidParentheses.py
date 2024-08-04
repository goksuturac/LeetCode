from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_bracket.values():
                stack.append(char)
            elif char in matching_bracket:
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False  

        return not stack 
solution = Solution()