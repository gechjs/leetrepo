class Solution:
    def totalMoney(self, n: int) -> int:
        
        count = 1
        ans = 0
        curr = 1
        for i in range(1, n+1):
            ans+=curr
            curr+=1
            if i%7 == 0:
                count +=1
                curr = count
                
        return ans
