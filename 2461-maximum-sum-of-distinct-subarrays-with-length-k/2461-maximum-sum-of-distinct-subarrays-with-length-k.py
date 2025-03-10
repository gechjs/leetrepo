class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        

        count = Counter()
        ans= 0
        sums = 0
        left = 0
        for i in range(k):
            sums+=nums[i]
            count[nums[i]]+=1
        if len(count)==k:
            ans = sums
        
        for right in range(k, len(nums)):
            sums+=nums[right]
            sums-=nums[left]
            count[nums[right]]+=1
            count[nums[left]]-=1
            if count[nums[left]]==0:
                del count[nums[left]]
            left+=1
            
            if len(count) == k:
                ans = max(ans, sums)
        return ans
