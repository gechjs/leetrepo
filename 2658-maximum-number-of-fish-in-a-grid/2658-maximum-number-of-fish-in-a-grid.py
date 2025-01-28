class Solution:
    def __init__(self):
        self.dir = [-1, 0, 1, 0, -1]

    def is_valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n

    def dfs(self, grid, visited, m, n, x, y):
        fish_count = grid[x][y]
        for i in range(4):
            new_x = x + self.dir[i]
            new_y = y + self.dir[i + 1]
            if self.is_valid(new_x, new_y, m, n) and not visited[new_x][new_y] and grid[new_x][new_y] > 0:
                visited[new_x][new_y] = True
                fish_count += self.dfs(grid, visited, m, n, new_x, new_y)
        return fish_count

    def findMaxFish(self, grid):
        m, n = len(grid), len(grid[0])
        max_fish = 0
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] > 0:
                    visited[i][j] = True
                    max_fish = max(max_fish, self.dfs(grid, visited, m, n, i, j))
        return max_fish