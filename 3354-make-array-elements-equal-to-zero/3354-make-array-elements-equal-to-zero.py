class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        
        _sum = 0
        total = sum(nums)
        ans  = 0 
        for i in range(len(nums)):
            _sum += nums[i]
            div = total//2
            if nums[i]==0 and _sum == div and div*2 == total:
                ans+=2
            elif nums[i]==0 and abs(total-(_sum*2))==1:
                ans+=1
        return ans

