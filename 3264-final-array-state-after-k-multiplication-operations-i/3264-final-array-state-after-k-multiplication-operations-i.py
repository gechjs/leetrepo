class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mins = min(nums)
            index = nums.index(mins)
            nums [index]*= multiplier
        return nums
            
