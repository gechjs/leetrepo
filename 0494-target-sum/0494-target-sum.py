class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ans = 0
        n = len(nums)
      
        def dp(i, curr):
            if i == n:
                if curr == target:
                    return 1
                return 0
            return dp(i+1, curr+nums[i])+dp(i+1, curr-nums[i])
            
       
        return dp(0, 0)
