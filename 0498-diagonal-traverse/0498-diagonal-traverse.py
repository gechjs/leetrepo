class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])
        
       
        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])
        
        result = []
        for key in sorted(diagonals.keys()):
            if key % 2 == 0:
                result.extend(reversed(diagonals[key]))  
            else:
                result.extend(diagonals[key]) 
        
        return result
