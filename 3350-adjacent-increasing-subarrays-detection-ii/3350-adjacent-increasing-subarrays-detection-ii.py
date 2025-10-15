class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        
        arr = []
        curr = 1
        for i in range(1, len(nums)):
            if nums[i]> nums[i-1]:
                curr+=1
            else:
                arr.append(curr)
                curr = 1
            
            if i == len(nums)-1:
                arr.append(curr)

        
        if len(arr) < 2:
            return arr[0]//2
        ans = 0
        for i in range(1, len(arr)):
            ans = max(ans, min(arr[i], arr[i-1]))
        print(arr)
        return max(ans, max(arr)//2)
