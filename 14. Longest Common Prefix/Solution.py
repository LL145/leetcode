class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i, t in enumerate(zip(*strs)):
            if len(set(t))>1: break
            ans += t[0]
        return ans
