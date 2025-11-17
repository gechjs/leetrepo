class Solution:
    def numSquares(self, n: int) -> int:
        
        squre = []
        for i in range(ceil(sqrt(n))+1):
            squre.append(i**2)

        dp = [n for _ in range(n+1)]
        dp[0] = 0
       
        for i in range(1, n+1):
            for j in range(len(squre)):
                if i-squre[j] < 0:
                    continue
                dp[i] = min(dp[i], dp[i-squre[j]]+1)
        print(dp)
        return dp[-1]
