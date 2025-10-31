class Solution:
    def lexSmallest(self, s: str) -> str:
       
        ans = s

        for i in range(len(s)):
            news = []
            j = i
            while j>=0:
                news.append(s[j])
                j-=1
            ans = min(ans, "".join(news)+s[min(i+1, len(s)-1):])
            j = len(s)-1
            news = []
            while j>=i:
                news.append(s[j])
                j-=1
            
            ans = min(ans, s[:i]+"".join(news))
          
        return ans

