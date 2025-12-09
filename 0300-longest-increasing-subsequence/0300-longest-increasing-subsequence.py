class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = defaultdict(int)
        def dp(i):
            if i in memo:
                return memo[i]
            for j in range(i+1, len(nums)):
        
                if nums[i]<nums[j]:
                    memo[i] = max(memo[i], 1+dp(j))
            memo[i] = max(memo[i], 1)
            return memo[i]
        ans = 0
        for i in range(len(nums)):
            if i in memo:
                ans = max(ans, memo[i])
                continue
            ans = max(ans, dp(i))
        
        return ans