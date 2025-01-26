class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        myset = set(nums)
        if len(myset)<3:
            return max(nums)
        myset.remove(max(myset))
        myset.remove(max(myset))

        return max(myset)
