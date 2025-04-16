class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        ans = 0
        dic = Counter()
        count = 0
        left = 0

        for right, val in enumerate(nums):
            dic[val]+=1
            count+=dic[val]-1
            while count>=k:
                ans+=len(nums)-right
                count-=(dic[nums[left]]-1)
                dic[nums[left]]-=1
                left+=1
        return ans 


