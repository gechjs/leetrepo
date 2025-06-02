class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue                
            left, right = i+1, len(nums)-1
            while right > left:
                sum = a + nums[right] + nums[left]
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    arr.append([a, nums[left], nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and right>left:
                        left+=1
        return arr