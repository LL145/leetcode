class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            sign = 1
        else:
            sign = -1
        y = sign*(int(str(abs(x))[::-1]))
        
        if -2**31 <y and y<2**31-1:
            return y
        else:
            return 0
