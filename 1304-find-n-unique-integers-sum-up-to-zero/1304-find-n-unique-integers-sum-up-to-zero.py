class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        ans = []

        if n & 1:
            ans.append(0)
            n-=1
        
        num = 1
        for _ in range(n//2):
            ans.append(num)
            ans.append(-1*num)
            n+=2
            num+=1
        
        return ans