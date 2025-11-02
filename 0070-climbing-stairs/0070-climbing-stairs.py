class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(num):
            if num == 0:
                return 1
            if num<0:
                return 0
        
            return dp(num-1)+dp(num-2)
        return dp(n)
