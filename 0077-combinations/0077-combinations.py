class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans  = []
        
        def backtrack(first, path):
            if len(path)==k:
                ans.append(path[:])
                return 

            for cand in range(first, n+1):
                path.append(cand)
                backtrack(cand+1, path)
                path.pop()
        backtrack(1, [])
        return ans