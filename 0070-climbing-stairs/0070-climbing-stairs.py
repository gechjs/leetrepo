class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1
        @cache
        def fun(num):
            
            if num==n:
                return 1
            if num==n-1:
                return fun(num+1)
            return fun(num+1) + fun(num+2)
        
        return fun(1)+fun(2)
