class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fre = Counter(nums)

        arr = list(fre.values())
        maxfre = max(arr)
        count = 0
        for i in range(len(arr)):
            if arr[i] == maxfre:
                count+=maxfre
        else:
            return count

            