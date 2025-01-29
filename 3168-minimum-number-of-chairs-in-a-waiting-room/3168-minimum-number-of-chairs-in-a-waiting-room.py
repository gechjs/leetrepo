class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        maxs = 0
        for i in s:
            if i=='E':
                count+=1
            else:
                count-=1
            maxs = max(maxs, count)
        return maxs