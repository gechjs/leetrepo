class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        count = Counter()
        for a, b in dominoes:
            key = (min(a, b), max(a, b))  
            count[key] += 1
        
        for n in count.values():
            ans += n * (n - 1) // 2 
        
        return ans