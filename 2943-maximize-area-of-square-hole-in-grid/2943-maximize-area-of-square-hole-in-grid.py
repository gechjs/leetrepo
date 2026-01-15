class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        h_max = self._find_longest_consective(hBars)
        v_max = self._find_longest_consective(vBars)
        
        max_size = min(h_max + 2, v_max + 2)
        return max_size * max_size

    def _find_longest_consective(self, arr: List[int]) -> int:
        is_cons = False
        tmp = 0
        res = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:
                is_cons = True
                tmp += 1
            else:
                is_cons = False
                tmp = 0
            
            if is_cons:
                res = max(res, tmp)
        return res 