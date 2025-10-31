class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        
        ans = 0
        for i, num in enumerate(nums):
            even = Counter()
            odd = Counter()
            
            for j in range(i, len(nums)):
                if nums[j] & 1:
                    odd[nums[j]]+=1
                else:
                    even[nums[j]]+=1
                if len(even)==len(odd):
                    ans = max(ans, j-i+1)
        return ans

        
