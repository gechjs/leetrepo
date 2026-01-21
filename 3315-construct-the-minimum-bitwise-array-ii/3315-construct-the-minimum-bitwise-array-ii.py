class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        
        for i in nums:
            if i == 2:
                ans.append(-1)
            else:
                cnt = 0
                j = i
                while (j & 1) == 1:
                    j >>= 1
                    cnt += 1
                
                cnt -= 1
                ans.append(i ^ (1 << cnt))
        
        return ans
