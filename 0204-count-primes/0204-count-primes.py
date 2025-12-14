class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<2:
            return 0
        arr = [1]*(n)
        arr[0], arr[1]=0, 0
        for num in range(2, ceil(sqrt(n))):
            curr = num*2
            while curr<n:
                arr[curr]=0
                curr+=num
        
        return sum(arr)