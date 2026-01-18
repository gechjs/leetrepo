class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
        prefix = [[arr[i] for i in range(len(grid[0]))] for arr in grid]
        
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if j-1>=0:
                    prefix[j][i]+=prefix[j-1][i]
                if i-1>=0:
                    prefix[j][i]+=prefix[j][i-1]
                
                if i-1>=0 and j-1>=0:
                    prefix[j][i]-=prefix[j-1][i-1]

        for k in range(min(len(grid[0]), len(grid)), 0, -1):
            
            for i in range(k-1, len(grid[0])):
                for j in range(len(grid)-k+1):
                    flag=True
                    _sum = prefix[j][i]
                    
                    if i-k>=0:
                        _sum-=prefix[j][i-k]
                    if j-1>=0:
                        _sum-=prefix[j-1][i]
                    if j-1>=0 and i-k>=0:
                        _sum+=prefix[j-1][i-k]
                    
                    curr = 0
                    diagonal=0
                    d = i
                    for l in range(j, j+k):
                        diagonal+=grid[l][d]
                        d-=1
                        curr = 0
                        curr+=prefix[l][i]
                        if i==3 and j==2 and k==3:
                            print(curr, "curr", grid[j][i])
                        if i-k>=0:
                            curr-=prefix[l][i-k]
                        if l-1>=0:
                            curr-=prefix[l-1][i]
                        if i-k>=0 and l-1>=0:
                            curr+=prefix[l-1][i-k]
                        if i==3 and j==2 and k==3:
                            print(curr, l, j)
                        if curr!=_sum:
                            flag=False
                            break
                   
                    if diagonal!=_sum:
                        flag = False
                    if not flag:
                        continue
                    diagonal = 0
                    d = j
                    for l in range(i-k+1, i+1):
                        diagonal+=grid[d][l]
                        d+=1
                        curr = prefix[j+k-1][l]
                        if j-1>=0:
                            curr-=prefix[j-1][l]
                        if l-1>=0:
                            curr-=prefix[j+k-1][l-1]
                        if l-1>=0 and j-1>=0:
                            curr+=prefix[j-1][l-1]
                        if i==3 and j==2 and k==3:
                            print(curr, l)
                        if _sum!= curr:
                            flag = False
                            break
                    if diagonal!=_sum:
                        flag=False
                    if flag:
                        return k
            
        return 1