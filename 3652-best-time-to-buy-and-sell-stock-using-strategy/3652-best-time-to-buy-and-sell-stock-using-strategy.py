class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        

        presum = []
        for i in range(len(prices)):
            presum.append(prices[i]*strategy[i])
        
        for i in range(1, len(presum)):
            presum[i]+=presum[i-1]

        for i in range(len(prices)):
            prices[i]+=prices[i-1]
        
        maxgain = 0
        gain = prices[k-1]-prices[k//2-1]-presum[k-1]
        for i in range(k, len(prices)):
            gain = prices[i-1]-prices[i//2-1]-presum[i-1]
            maxgain = max(maxgain, gain)
        return maxgain+presum[-1]
