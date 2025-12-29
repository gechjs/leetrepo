class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
      
        graph = defaultdict(set)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    graph[(i, j)] = set()
                    if i-1>=0:
                        if grid[i-1][j] == "1":
                           graph[(i, j)].add((i-1, j))
                           graph[(i-1, j)].add((i, j))
                    if i+1<len(grid):
                        if grid[i+1][j]== "1":
                            graph[(i, j)].add((i+1, j))
                            graph[(i+1, j)].add((i, j))
                        
                    if j-1>=0:
                        if grid[i][j-1] == "1":
                            graph[(i, j)].add((i, j-1))
                            graph[(i, j-1)].add((i, j))

                    if j+1<len(grid[0]):
                        if grid[i][j+1]== "1":
                            if grid[i][j+1]== "1":
                                graph[(i, j)].add((i, j+1))
                                graph[(i, j+1)].add((i, j))
        visited = set()
        ans = 0
        for node in graph:
            if node not in visited:
                visited.add(node)

                stack = [node]

                while stack:
                    curr = stack.pop()

                    for neighbours in graph[curr]:
                        if neighbours not in visited:
                            visited.add(neighbours)
                            stack.append(neighbours)
                ans+=1
        return ans