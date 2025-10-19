class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1
        @cache
        def fun(num):
            
            if num==1 or num == 0:
                return 1
            return fun(num-1) + fun(num-2)
        
        return fun(n)
