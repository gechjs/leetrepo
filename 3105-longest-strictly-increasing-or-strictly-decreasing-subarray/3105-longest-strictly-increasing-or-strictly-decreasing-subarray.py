class Solution:
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        longest = 1
        strictly_increasing = 1
        strictly_decreasing = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                strictly_increasing += 1
                strictly_decreasing = 1
            elif nums[i] < nums[i - 1]:
                strictly_decreasing += 1
                strictly_increasing = 1
            else:
                strictly_increasing = 1
                strictly_decreasing = 1
            
            longest = max(longest, strictly_increasing, strictly_decreasing)
        
        return longest