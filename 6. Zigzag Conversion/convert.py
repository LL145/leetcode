class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ['' for _ in range(numRows)]
        curr_row = 0
        for c in s:
            res[curr_row] += c
            if curr_row == 0: direction = 1
            elif curr_row == numRows - 1: direction = -1
            curr_row = (direction + curr_row) % numRows
        return ''.join(res)
