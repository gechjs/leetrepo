class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        ans = 0
        for row in grid:
            for i in range(len(row)):
                if row[i]<0:
                    ans+=len(row)-i
                    break
        return ans