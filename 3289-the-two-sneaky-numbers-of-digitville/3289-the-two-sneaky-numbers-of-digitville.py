class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for key in count:
            if count[key]>1:
                ans.append(key)
        return ans