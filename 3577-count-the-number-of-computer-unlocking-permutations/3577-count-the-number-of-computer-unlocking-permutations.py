class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        
        
        minval = min(complexity)
        second = min(complexity[1:])

        if complexity[0] != minval or minval==second:
            return 0
        
        ans = 1
        for i in range(1, len(complexity)):
            ans*=i
        return ans%(10**9 + 7)
        
