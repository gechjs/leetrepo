class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp[0][0]+=1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row-1>=0:
                    dp[row][col]+=dp[row-1][col]
                if col-1>=0:
                    dp[row][col]+=dp[row][col-1]
                
                if obstacleGrid[row][col]== 1:
                    dp[row][col] = 0
        
        return dp[-1][-1]
        