class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        myset  = set()

        for num in arr:
            if num%k in myset:
                myset.remove(num%k)
            else:
                myset.add((k-num%k)%k)
           
        
        return len(myset)==0