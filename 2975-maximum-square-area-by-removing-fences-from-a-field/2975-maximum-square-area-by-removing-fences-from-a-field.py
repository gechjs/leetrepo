class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        ans = -1
        seth = set([n, *vFences])
        if m in seth:
            print(m)
            return (m-1)**2
        for num in hFences:
            if num in seth:
                ans = max(ans, (num-1)**2)
                print(num)
        
        return ans