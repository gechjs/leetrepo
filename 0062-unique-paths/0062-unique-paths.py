class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dp(i, j):
    
            if i==m or j==n:
                return 1


            if (i, j) not in memo:
                memo[(i, j)] = dp(i+1, j)+dp(i, j+1)
            return memo[(i, j)]
        
        return dp(1, 1)
            
        