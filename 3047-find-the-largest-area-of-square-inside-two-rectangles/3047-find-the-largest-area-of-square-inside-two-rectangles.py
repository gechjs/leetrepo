class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        ans = 0
       
        for i in range(len(bottomLeft)-1):
            for j in range(i+1, len(bottomLeft)):
                
                bx = max(bottomLeft[i][0], bottomLeft[j][0])
                by = max(bottomLeft[i][1], bottomLeft[j][1])
                tx = min(topRight[i][0], topRight[j][0])
                ty = min(topRight[i][1], topRight[j][1])

                if tx>bx and ty>by:
                    ans = max(ans, min(tx-bx, ty-by)**2)
                   
        return ans