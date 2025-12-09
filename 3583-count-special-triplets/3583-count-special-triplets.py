class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        left = Counter()

        right = Counter(nums)
        ans = 0
        for num in nums:
            right[num]-=1
            ans+=left[num*2]*right[num*2]
            left[num]+=1
            
            
        return ans%(10**9+7)
