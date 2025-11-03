class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        n  = len(colors)

        left = 0
        
        ans = 0
        for right in range(n):
            if colors[right] !=  colors[left]:
                if right-left>=2:
                    ans+=(sum(neededTime[left:right])-max(neededTime[left:right]))
                left = right
        
        if right-left>=1:
            ans+=(sum(neededTime[left:right+1])-max(neededTime[left:right+1]))
        return ans
