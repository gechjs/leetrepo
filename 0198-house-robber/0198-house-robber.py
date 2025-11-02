class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        def dp(i):
            if i >= n:
                return 0
            if i == n-1:
                return nums[i]
            if i not in memo:
                memo[i] = max(dp(i+1), nums[i]+dp(i+2))
            return memo[i]
        return dp(0)