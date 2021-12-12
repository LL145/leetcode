class Solution:
    def isValid(self, s: str) -> bool:
        pair={')':'(', ']':'[', '}':'{'}
        left = {'(', '{', '['}
        right = {')', '}', ']'}
        stack = []
        for c in s:
            if c in left: stack.append(c)
            if c in right:
                if not stack: return False
                if not pair[c] == stack.pop(): return False
        return not stack
