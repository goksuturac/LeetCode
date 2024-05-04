from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
# solution 1:
        alph_list = sorted(strs)
        first_char = alph_list[0]
        last_char = alph_list[-1]
        for i in range(len(first_char)):
            if first_char[i] != last_char[i]:
                break
            output += first_char[i]
        return output
# solution 2:
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return output
        #     output += strs[0][i]
        # return output