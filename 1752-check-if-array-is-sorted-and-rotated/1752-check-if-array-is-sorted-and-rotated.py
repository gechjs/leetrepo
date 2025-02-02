class Solution:
    def check(self, nums: List[int]) -> bool:
        
        track = False
        for i in range(len(nums)):
            if track:
                if i == len(nums)-1:
                    if nums[i]>nums[0]:
                        return False
                    else:
                        return True
                if nums[i+1]<nums[i]:
                    return False
            elif i == len(nums)-1:
                    return True
            elif nums[i+1]<nums[i]:
                track = True
                
              
                

