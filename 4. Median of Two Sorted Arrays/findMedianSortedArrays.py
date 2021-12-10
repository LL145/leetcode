class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1
            if l1[0] < l2[0]:
                return [l1[0]] + merge(l1[1:], l2)
            else:
                return [l2[0]] + merge(l1, l2[1:])
            
        nums = merge(nums1,nums2)
        l = len(nums)
        if l%2:
            return nums[(l-1)//2]
        else:
            return (nums[l//2] +nums[l//2 -1])/2
