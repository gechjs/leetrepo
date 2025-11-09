class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        ans = set()
        def dp(curr, val):
            nonlocal ans
            if curr>amount:
                return 
            if curr == amount:
                ans.add(val)
                return
            for num in coins:
                dp(curr+num, val+1)
        
        dp(0, 0)
        return -1 if len(ans) == 0 else min(ans)


            

            
       
        