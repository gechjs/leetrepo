class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        num = math.log(n, 4)
        if math.floor(num)==num:
            return True
        return False