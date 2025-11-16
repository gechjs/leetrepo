class Solution:
    def numSub(self, s: str) -> int:
        
        curr = 0
        ans = 0
        for right in range(len(s)):
            if s[right]=="1":
                curr+=1
                ans+=curr
            else:
                curr=0
        return ans%(10^9 + 7)
