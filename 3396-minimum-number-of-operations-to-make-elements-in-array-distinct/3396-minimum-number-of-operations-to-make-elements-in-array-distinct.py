class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        right = len(nums) - 1
        count = Counter()
        while right >= 0:
            if count[nums[right]]>0:
                if (right+1)%3 != 0:
                    return (right+1)//3 + 1
                return (right+1)//3
            count[nums[right]]+=1
            right -=1
        return 0
