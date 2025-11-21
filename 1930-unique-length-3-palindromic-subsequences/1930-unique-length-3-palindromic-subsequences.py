class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        right = Counter(s[1:])
        left = Counter()
        left[s[0]]+=1
        ans = 0
       
        seen = set()
        for i in range(1, len(s)-1):

            right[s[i]]-=1
            if right[s[i]]==0:
                del right[s[i]]
            
            for key in left:
                if key in right and (key, s[i]) not in seen:
                    ans+=1
                    seen.add((key, s[i]))
            left[s[i]]+=1
        
        return ans
