class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        startTime = [jobs[i][0] for i in range(n)]
        @lru_cache(None)
        def dp(i): # maximum profit taking jobs in jobs[i...n-1]
            if i == n: return 0
            j = bisect_left(startTime, jobs[i][1])
            return max(dp(i + 1), dp(j) + jobs[i][2])
        return dp(0)
            
        
