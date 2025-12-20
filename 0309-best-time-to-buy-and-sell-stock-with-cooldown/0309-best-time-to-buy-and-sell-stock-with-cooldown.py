class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
      
        @cache
        def dp(i, t_type):
            if i>=len(prices):
                return 0
            if t_type==False:
                return max(prices[i]+dp(i+2, True), dp(i+1, False)) 
            else:
                return max(max(-1*prices[i]+dp(i+1, False), dp(i+1, True)), 0)
                
        return dp(0, True)
