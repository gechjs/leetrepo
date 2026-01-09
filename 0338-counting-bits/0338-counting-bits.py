class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        for i in range(n+1):
            j = i
            count = 0
            while j>0:
                count+=j%2
                j = j//2
            ans.append(count)
        
        return ans