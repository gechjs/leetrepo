class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        j = 0
        ans = 0
        for i in range(len(g)):
            if j>=len(s):
                break
            if s[j]>=g[i]:
                j+=1
                ans+=1
            else:
                while  j<len(s):
                    if s[j]>=g[i]:
                        ans+=1
                        j+=1
                        break
                    j+=1
        return ans

