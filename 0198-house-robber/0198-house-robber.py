class Solution:
    def rob(self, nums: List[int]) -> int:
        
      n = len(nums)

      memo = {}
      def dp(i):
        if i>=n:
            return 0
        if i == n-1:
            return nums[i]
        
        if i not in memo:
            take = dp(i+2)+nums[i]
            skip = dp(i+1)
            memo[i] = max(take, skip)

        return memo[i]
      
      return dp(0)