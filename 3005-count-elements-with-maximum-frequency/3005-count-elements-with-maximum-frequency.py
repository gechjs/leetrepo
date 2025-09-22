class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        maxval = max(count.values())

        ans = 0

        for num in count.values():
            if num == maxval:
                ans+= maxval
        return ans


            