class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        flag = True 
        num = n+1
        while flag:
            count = Counter(str(num))
            for key, val in count.items():
                if int(key) != val:
                    break
            else:
                return num
        
            num+=1