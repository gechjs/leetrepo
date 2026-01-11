class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[int(s) for s in row] for row in matrix]

        flag = 0; c = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j]:
                    flag = 1; c+= 1
                    if i > 0:
                        dp[i][j] += dp[i-1][j]

        if not flag:
            return 0

        if c == 1:
            return 1

        res = 0
        def max_rec_area(row)->None:
            nonlocal res
            row.append(0)
            st = [] # increasing stack

            for i in range(len(row)):
                while st and row[i] < row[st[-1]]:
                    h = row[st.pop()]
                    if not st:
                        w = i

                    else:
                        w = i - st[-1] - 1 

                    res = max(res, h*w)

                st.append(i)

        for row in dp:
            max_rec_area(row)

        return res


