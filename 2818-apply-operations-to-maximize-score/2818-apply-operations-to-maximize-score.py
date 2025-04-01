class Solution:
    def prime_score(self, x):
        score = 0
        i = 2
        while i * i <= x:
            if x % i == 0:
                score += 1
                while x % i == 0:
                    x //= i
            i += 1
        if x > 1:
            score += 1
        return score

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        prime_scores = [self.prime_score(x) for x in nums]

        left = [1] * n
        right = [1] * n

        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        elements = []
        for i in range(n):
            count = left[i] * right[i]
            elements.append((-nums[i], i, count))

        heapq.heapify(elements)

        score = 1
        while k > 0 and elements:
            neg_val, i, cnt = heapq.heappop(elements)
            val = -neg_val
            take = min(k, cnt)
            score = pow(val, take, MOD) * score % MOD
            k -= take

        return score
