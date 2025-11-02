class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        @cache
        def dp(i, curr):
            if i>=n:
                return curr
            
            return cost[i] + min(dp(i+1, curr), dp(i+2, curr))
        return min(dp(0, 0), dp(1, 0))
        