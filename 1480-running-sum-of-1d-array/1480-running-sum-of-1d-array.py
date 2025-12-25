class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = [nums[0]]

        for num in nums[1:]:
            ans.append(ans[-1]+num)
        return ans