class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
      
        longest = 0
        if len(nums)==0:
            return 0

        left = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count+=1
            if zero_count > 1:
                while zero_count>1:
                    if nums[left] == 0:
                        zero_count-=1
                    left+=1
            longest = max(longest, right-left+1)
        return longest-1