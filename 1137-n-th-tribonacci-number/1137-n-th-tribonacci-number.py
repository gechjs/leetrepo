class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = [0, 1, 1]
        if n<=2:
            return dp[n]
        
        for i in range(3, n+1):
            middle = dp[2]
            last = dp[1]
            dp= [last, middle , sum(dp)]
        return dp[-1]
            