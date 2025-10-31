class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        seen = set(nums)
        for i in range(1, len(nums)+1):
            if i*k not in seen:
                return i*k
        return i*k+k

