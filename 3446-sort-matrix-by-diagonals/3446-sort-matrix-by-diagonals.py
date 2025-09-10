class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for r in range(n):
            i, j = r, 0
            vals, cells = [], []
            while i < n and j < n:
                vals.append(grid[i][j])
                cells.append((i, j))
                i += 1
                j += 1
            vals.sort(reverse=True)  # non-increasing
            for (i, j), v in zip(cells, vals):
                grid[i][j] = v


        for c in range(1, n):
            i, j = 0, c
            vals, cells = [], []
            while i < n and j < n:
                vals.append(grid[i][j])
                cells.append((i, j))
                i += 1
                j += 1
            vals.sort()  # non-decreasing
            for (i, j), v in zip(cells, vals):
                grid[i][j] = v

        return grid
