class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = ""
        for r in range(numRows):
            jumping_step = 2 * numRows - 2
            for i in range(r,len(s), jumping_step):
                result += s[i]
                if (r > 0 and r < numRows -1 and i + jumping_step - 2 * r < len(s)):
                    result += s[i + jumping_step - 2 * r]
        return result