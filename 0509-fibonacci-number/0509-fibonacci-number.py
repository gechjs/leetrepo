class Solution:
    def fib(self, n: int) -> int:

        def fibo(num):
            if num<=1:
                return num
            
            return fibo(num-1)+fibo(num-2)
        
        return fibo(n)


      