class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0         
        curr_sum = 0   
        count = 0

        while left < n:
            while right < n and (curr_sum + nums[right]) * (right - left + 1) < k:
                curr_sum += nums[right]
                right += 1
            count += right - left
            if right == left:
                right += 1
            else:
                curr_sum -= nums[left]

            left += 1

        return count