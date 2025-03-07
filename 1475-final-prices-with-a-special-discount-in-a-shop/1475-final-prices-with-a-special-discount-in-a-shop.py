class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        ans = [0]*(len(prices))
        for i in range(len(prices)-1, -1, -1):
            while stack and prices[i] < stack[-1]:
                stack.pop()
            
            ans[i]=prices[i]-stack[-1] if stack else prices[i]
            stack.append(prices[i])
        return ans