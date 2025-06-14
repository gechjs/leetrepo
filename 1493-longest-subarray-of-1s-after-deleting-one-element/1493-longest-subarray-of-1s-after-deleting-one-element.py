class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left , maxlen , zero  = 0 , 0 , 0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            while(zero>1):
                if nums[left]==0:
                    zero-=1
                left += 1
            maxlen = max(maxlen , i-left+1 )
        return maxlen-1

