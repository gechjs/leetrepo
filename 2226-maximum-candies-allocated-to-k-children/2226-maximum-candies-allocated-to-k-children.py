class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        _sum = sum(candies)
        if _sum< k:
            return 0
        if _sum == k:
            return 1
        
        left = 0
        right = _sum

        ans = 0
        def check(n):
            curr = 0
            for num in candies:
                curr+= num//n
            return curr>= k
        while right>=left:
            mid = (right+left)//2

            if check(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return ans
            
                