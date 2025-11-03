class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return max(nums)
        temp = nums.copy()
        for i in range(1, len(nums)-1):
            if i == 1:
                nums[i] = max(nums[:2])
                continue

            nums[i]= max(nums[i]+nums[i-2], nums[i-1])

        ans = nums[-2]
        nums = temp
        for i in range(2, len(nums)-1):
            if i == 2:
                nums[i] = max(nums[1:3])
                continue

            nums[i]= max(nums[i]+nums[i-2], nums[i-1])

        ans = max(ans, nums[-1])
        return ans