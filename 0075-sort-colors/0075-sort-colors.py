class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i],nums[red] = nums[red], nums[i]
                red+=1
        for j in range(red, len(nums)):
            if nums[j] == 1:
                nums[j], nums[red] = nums[red], nums[j]
                red+=1

        for j in range(red, len(nums)):
            if nums[j] == 2:
                nums[j], nums[red] = nums[red], nums[j]
                red+=1

            
        