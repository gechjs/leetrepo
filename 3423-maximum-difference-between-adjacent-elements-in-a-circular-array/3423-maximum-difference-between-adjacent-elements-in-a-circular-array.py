class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxdiff = 0
        for i in range(len(nums)):
            if i == len(nums)-1:
                maxdiff = max(maxdiff, abs(nums[i]-nums[0]))
            else:  
                maxdiff = max(maxdiff, abs(nums[i]-nums[i+1]))
        return maxdiff