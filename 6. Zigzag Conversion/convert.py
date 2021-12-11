class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows= [''] * numRows
        r = 0
        d = -1
        for c in s:
            rows[r] += c
            if r ==0 or r == numRows-1:
                d = -d
            r += d
        return ''.join(rows)
