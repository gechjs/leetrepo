class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        myset = set()
        for i in ranges:
            for j in range(i[0], i[1]+1):
                myset.add(j)
        for k in range(left, right+1):
            if k not in myset:
                return False
        return True
                
