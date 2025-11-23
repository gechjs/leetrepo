class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        

        ans = 0 

        def dp(i, sums):
            nonlocal ans

            if i>=len(nums):
                return

            if (sums+nums[i])%3 == 0:
                ans = max(ans, sums+nums[i])
            
            
            for j in range(i+1, len(nums)):
                dp(j, sums+nums[i])
        
        for k in range(len(nums)):
            dp(k, 0)
        
        return ans
