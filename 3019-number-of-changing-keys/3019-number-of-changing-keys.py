class Solution:
    def countKeyChanges(self, s: str) -> int:
        def swapCase(t):
            if t == t.upper():
                return t.lower()
            else:
                return t.upper()
        count = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1] and s[i] != s[i-1].swapcase():
                count+=1
        return count
