class Solution:
    def minBitwiseArray(self, nums):
        n = len(nums)
        ans = [0] * n
        
        for i in range(n):
            val = float('inf')
            for j in range(nums[i]):
                if (j | (j + 1)) == nums[i]:
                    val = min(val, j)
                    break
            
            if val == float('inf'):
                ans[i] = -1
            else:
                ans[i] = val
        
        return ans
