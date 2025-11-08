class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        m = n
        while m:
            m >>= 1
            n ^= m
        return n
