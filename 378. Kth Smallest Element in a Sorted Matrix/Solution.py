class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        for _ in range(k):
            num, row, col = heappop(heap)
            for i, j in ((row+1, col), (row, col+1)):
                if i < n and j < n and matrix[i][j] is not None:
                    heappush(heap, (matrix[i][j], i, j))
                    matrix[i][j] = None
        return num
