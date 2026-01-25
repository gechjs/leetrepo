class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        nums.sort()
        for i in range(k-1, len(nums)):
            ans = min(ans, nums[i]-nums[i-k+1])
        return ans