class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for x, y in guards:
            matrix[x][y] = 'G'

        for x, y in walls:
            matrix[x][y] = 'W'

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(x, y, dx, dy):
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            if matrix[x][y] in ('G', 'W'):
                return
            if matrix[x][y] == 0:
                matrix[x][y] = 'V'
            dfs(x + dx, y + dy, dx, dy)

        for x, y in guards:
            for dx, dy in directions:
                dfs(x + dx, y + dy, dx, dy)

        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    count += 1

        return count
