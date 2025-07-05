class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        count = Counter(arr)
        ans = []
        for key, value in count.items():
            if key == value:
                ans.append(value)
        return  max(ans) if ans else -1 