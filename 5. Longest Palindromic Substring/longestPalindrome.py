class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def longp(s, center):
            start = center[0]
            end = center[-1]
            out = s[start:end+1]
            l = end- start+1
            while start>0 and end < n-1:
                start = start-1
                end = end+1
                if s[start] == s[end]:
                    l = l+2
                    out = s[start:end+1]
                    
                else:
                    return l, out
            return l, out
        
        m = 0
        out = ""
        
        for i in range(n):
            l, o = longp(s, [i])
            if l>m:
                m = l
                out = o
        for i in range(n-1):
            if s[i] == s[i+1]:
                l, o = longp(s, [i,i+1])
                if l>m:
                    m=l
                    out = o
        return out
