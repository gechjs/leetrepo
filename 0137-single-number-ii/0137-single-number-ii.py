class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i == 0:
                if nums[i+1]!=nums[i]:
                    return nums[i]
            elif i == len(nums)-1:
                if nums[i] != nums[i-1]:
                    return nums[i]
            else:
                if nums[i]!=nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]

                

        