class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        maxval = max(sum1+nums1.count(0), sum2+nums2.count(0))
        
        if sum1+nums1.count(0) < maxval and nums1.count(0) == 0:
            return -1
        if sum2+nums2.count(0) < maxval and nums2.count(0)==0:
            return -1
        
        return maxval
