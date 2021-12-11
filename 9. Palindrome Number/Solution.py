class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        inputNum = x
        newNum = 0
        while x:
            newNum = 10 * newNum + x % 10
            x = x // 10
        return newNum == inputNum
        
