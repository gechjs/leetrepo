class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        small = min(nums)
        large = max(nums)

        for num in range(small, 0, -1):
            if large%num == 0 and small%num == 0 :
                return num


