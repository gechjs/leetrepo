class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        maxl = 0

        pre_map = {0: -1}
        curr = 0
        for i in range(len(nums)):
            curr+= nums[i]*2-1
            if curr in pre_map:
                maxl = max(maxl, i-pre_map[curr])
            else:
                pre_map[curr] = i
        return maxl