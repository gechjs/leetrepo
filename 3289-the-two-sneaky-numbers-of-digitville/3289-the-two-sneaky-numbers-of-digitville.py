class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        ans = []
        seen = set()
        for num in nums:
            if num in seen:
                ans.append(num)
                if len(ans)==2:
                    break
            else:
                seen.add(num)
        return ans