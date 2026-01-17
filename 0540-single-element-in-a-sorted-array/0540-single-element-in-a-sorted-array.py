class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1

        def check(num):
            if nums[num-1]==nums[num]:
                if (num-1)&1:
                    return False
            else:
                if num&1:
                    return False

            return True
                
        
        while right>=left:
            mid = (right+left)//2
            if mid==0:
                return nums[0]
            if mid==len(nums)-1:
                return nums[-1]
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if check(mid):
                left = mid+1
            else:
                right = mid-1