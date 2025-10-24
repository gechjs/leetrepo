class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        def is_palindrome(x):
            right, left = len(x)-1, 0
            flag = True 
            while right>left:
                if x[right] ==  x[left]:
                    right-=1
                    left+=1
                else:
                    flag = False
                    break
            return flag
        
        if is_palindrome(a) or is_palindrome(b):
            return True
        x, y, = a, b
        def check(a, b):
            left, right = 0, len(a)-1
            count = 0
            while right>left:
                if a[left] == b[right]:
                    count+=1
                    left+=1
                    right-=1
                else:
                    break
            
            if is_palindrome(a[left:right+1]) or is_palindrome(b[left:right+1]):
                return True
            else:
                return False
            
        return True if check(x, y) or check(y, x) else False