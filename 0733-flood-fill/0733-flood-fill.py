class Solution:
    def floodFill(self, img: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(img), len(img[0])
        old = img[sr][sc]
        if old == newColor:
            return img

        def dfs(x, y):
            if (x < 0 or y < 0 ) or (x >= m or y >= n) or (img[x][y] != old):
                return
            img[x][y] = newColor
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        dfs(sr, sc)
        return img
