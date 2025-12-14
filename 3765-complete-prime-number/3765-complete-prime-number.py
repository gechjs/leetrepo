class Solution:
    def completePrime(self, num: int) -> bool:


        s = str(num)
        def isPrime(n):
            i = 2
            if int(n)<=1:
                return False
            if int(n)==2:
                return True
            while i<=ceil(sqrt(int(n))):
                if int(n)%i==0:
                    return False
                i+=1
            return True
        for i in range(len(s)):
            if not isPrime(s[i:]) or not isPrime(s[:i+1]):
                return False
        
        return True

    