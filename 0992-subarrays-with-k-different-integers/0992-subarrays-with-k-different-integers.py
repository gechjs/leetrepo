class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        less_or_equal = 0

        left = 0

        count = Counter()
        less = 0

        for right in range(len(nums)):
            count[nums[right]]+=1
            while len(count)>k:
                count[nums[left]]-=1
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1

            less_or_equal+=right-left+1

        left = 0
        count = Counter()
        less = 0

        for right in range(len(nums)):
            count[nums[right]]+=1
            while len(count)>=k:
                count[nums[left]]-=1
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1
                
            less+=right-left+1
        
        return less_or_equal-less