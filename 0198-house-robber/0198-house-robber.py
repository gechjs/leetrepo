class Solution:
    def rob(self, nums: List[int]) -> int:
        
        for i, num in enumerate(nums):
            if i==0:
                continue
            if i==1:
                nums[i] = max(nums[0], nums[1])
            nums[i] = max(nums[i]+nums[i-2], nums[i-1])
        return nums[-1]
        