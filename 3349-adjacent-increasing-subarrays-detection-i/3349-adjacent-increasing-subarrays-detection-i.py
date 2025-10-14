class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def is_increasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        for a in range(n - 2 * k + 1):
            if is_increasing(a) and is_increasing(a + k):
                return True

        return False
