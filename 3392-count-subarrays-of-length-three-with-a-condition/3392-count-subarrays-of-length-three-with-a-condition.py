class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        count = 0
        for right in range(2, len(nums)):
            if nums[right]+nums[right-2]==nums[right-1]/2:
                count+=1
        return count
