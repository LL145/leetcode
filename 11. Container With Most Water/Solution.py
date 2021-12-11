class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        m = 0
        l, r = 0, N-1
        while l < r:
            area = min(height[l],height[r])*(r-l)
            if area > m:
                m = area
            if height[l]<height[r]:
                l = l+1
            else:
                r = r-1
        return m
