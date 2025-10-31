class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        snums = sorted(nums)

        if snums[-2]*2<=snums[-1]:
            return nums.index(snums[-1])
        return -1