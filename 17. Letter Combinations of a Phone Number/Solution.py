class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        kvmaps = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl',
                  '6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}
        ans = ['']
        for d in digits: ans = [word + c for word in ans for c in kvmaps[d]]
        return ans
