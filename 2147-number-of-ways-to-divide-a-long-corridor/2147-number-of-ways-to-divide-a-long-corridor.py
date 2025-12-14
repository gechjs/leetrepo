class Solution:
    MOD = 10**9 + 7

    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        dp = [[-1] * 3 for _ in range(n + 1)]

        def f(i: int, cnt: int) -> int:
            if i == n:
                return 1 if cnt == 2 else 0

            if dp[i][cnt] != -1:
                return dp[i][cnt]

            ch = corridor[i]
            if ch == 'S':
                cnt += 1

            if cnt > 2:
                return 0

            if cnt < 2:
                dp[i][cnt] = f(i + 1, cnt) % self.MOD
                return dp[i][cnt]

            broke = f(i + 1, 0) % self.MOD
            notbreak = f(i + 1, cnt) % self.MOD
            dp[i][cnt] = (broke + notbreak) % self.MOD
            return dp[i][cnt]

        return f(0, 0) % self.MOD
