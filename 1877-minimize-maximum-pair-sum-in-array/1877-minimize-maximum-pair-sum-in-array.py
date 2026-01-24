class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        ans = 0
        for i in range(len(nums)//2):
            ans = max(ans, nums[i]+nums[-1*(i+1)])
        return ans