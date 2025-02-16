class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if len(s)==1:
            return True
        left = 0
        count = Counter()
        for i in range(k):
            count[s[i]]+=1
        if len(s)>k:
            if len(count)==1 and s[k]!=s[0]:
                return True 
        elif len(s)==k:
            if len(count)==1:
                return True
            else:
                return False
        for right in range(k, len(s)):
            count[s[right]]+=1
            count[s[left]]-=1
            if count[s[left]]==0:
                del count[s[left]]
            
            print(count[s[left]])
            if right == len(s)-1 and len(count) ==1 and s[left] != s[right]:
                return True
            elif len(count)==1 and s[left] != s[right] and s[right] != s[right+1]:
                return True
            left+=1
        return False
