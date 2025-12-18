class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        prefixPrice = [0] * (n + 1)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixPrice[i] = prefixPrice[i-1] + prices[i]
            prefixSum[i] = prefixSum[i-1] + strategy[i] * prices[i]
        ans = prefixSum[-2]
        for i in range(n+1-k):
            start = i            
            end = i + k - 1
            mid = i + k // 2
            tmp = prefixSum[-2] - (prefixSum[i+k-1] - prefixSum[i-1])
            t = tmp + prefixPrice[end] - prefixPrice[mid-1]
            ans = max(ans, t)
        return ans
            