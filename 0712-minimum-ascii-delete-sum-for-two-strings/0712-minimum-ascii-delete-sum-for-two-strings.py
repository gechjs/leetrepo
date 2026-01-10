class Solution:
    def solve(self, i: int, j: int, s1: str, s2: str, dp: List[List[int]]) -> int:
        if i == 0 and j == 0:
            return 0

        if i == 0:
            ans = 0
            while j > 0:
                ans += ord(s2[j-1])
                j -= 1
            return ans

        if j == 0:
            ans = 0
            while i > 0:
                ans += ord(s1[i-1])
                i -= 1
            return ans

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i-1] == s2[j-1]:
            dp[i][j] = self.solve(i-1, j-1, s1, s2, dp)
        else:
            dp[i][j] = min(
                ord(s1[i-1]) + self.solve(i-1, j, s1, s2, dp),
                ord(s2[j-1]) + self.solve(i, j-1, s1, s2, dp)
            )
        return dp[i][j]

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        return self.solve(n, m, s1, s2, dp)
