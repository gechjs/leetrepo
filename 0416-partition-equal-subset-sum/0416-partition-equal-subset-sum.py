class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if 1 & sum(nums):
            return False
        
        half = sum(nums)//2
        seen = set([0])

        for num in nums:
            myset  = seen.copy()
            for n in myset:
                seen.add(n+num)
            if half in seen:
                return True
        return False
        # track = False
        # def dp(arr, _sum):
        #     nonlocal track
        #     if not arr:
        #        return 
        #     if arr[0]+_sum> half:
        #         dp(arr[1:], _sum)
        #         return
        #     if arr[0]+_sum == half:
        #         track = True
        #         return 
        #     else:
        #         dp(arr[1:], _sum+arr[0])
        #         dp(arr[1:], _sum)

        # dp(nums, 0)
        # return track

                




