class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]   

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dp[row][col] = grid[row][col]
                if row-1>=0 and col-1>=0:
                    dp[row][col]+=min(dp[row-1][col], dp[row][col-1])
                elif row-1>=0:
                    dp[row][col] += dp[row-1][col]
                elif col-1>=0:
                    dp[row][col]+= dp[row][col-1]
       
        return dp[-1][-1]