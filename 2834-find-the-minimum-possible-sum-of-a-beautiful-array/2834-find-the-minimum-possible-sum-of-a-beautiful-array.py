class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        
        half_t = n-(target-1)//2
        right_half = n+(target)//2
        if target>=n*2:
            return n*(n+1)//2
        if target<=n:
            half = target//2
            diff = target-1-half

            upper = n+diff

            return upper*(upper+1)//2-(target+half)*diff//2
        

        half = target//2
        diff = n-half
        upper = n+diff

        return upper*(upper+1)//2-(n+half+1)*diff//2

    

