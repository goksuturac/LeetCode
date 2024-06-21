from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        stringMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        
        result = []
        def backtrack(i,path):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            
            for letter in stringMap[digits[i]]:
                path.append(letter)
                backtrack(i+1, path)
                path.pop()

        backtrack(0,[])
        return result

 