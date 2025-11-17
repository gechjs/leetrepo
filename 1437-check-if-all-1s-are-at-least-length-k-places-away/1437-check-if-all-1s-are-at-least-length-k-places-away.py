class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        stack = []

        for i in range(len(nums)):
            if nums[i] == 1:
                if stack and i - stack[-1] <= k:
                    return False
                else:
                    stack.append(i)
        return True