class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        mat = [[0]*n for _ in range(n)]
        
        prefix = [[0]*(n+1) for _ in range(n+1)]

        for arr in queries:
            r1, c1, r2, c2 = arr
            prefix[r1][c1]+=1
            prefix[r1][c2+1]-=1
            prefix[r2+1][c2+1]+=1
            prefix[r2+1][c1]-=1

        
        for i in range(n):
            for j in range(n):
                if i>0 and j>0:
                    prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+prefix[i][j]
                elif i>0 and j==0:
                    prefix[i][j] = prefix[i-1][j]+prefix[i][j]
                elif i==0 and j>0:
                    prefix[i][j] = prefix[i][j-1]+prefix[i][j]

        for i in range(n):
            for j in range(n):
                mat[i][j] = prefix[i][j]
        return mat