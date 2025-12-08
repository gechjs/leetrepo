class Solution:
    def countTriples(self, n: int) -> int:
        
        ans = 0
        myset = set()
        for i in range(1, n+1):
            myset.add(i*i)
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i*i + j*j in myset:
                    ans+=1
        return ans