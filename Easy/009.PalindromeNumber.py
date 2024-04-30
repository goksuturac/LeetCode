class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return(str(x) == str(x)[::-1])
        if x <0: return False

        num_reverse = 0
        digit = 0
        while(x // (10**digit) != 0):
            num_reverse = (num_reverse * 10) + (x // (10**digit) % 10)
            digit += 1
        return(x == num_reverse)