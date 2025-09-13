class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowel = ["a", "e", "u", "i", "o"]
        count = Counter(s) 

        maxv = 0
        maxc = 0
        for char in s:
            if char in vowel:
                maxv = max(maxv, count[char])
            else:
                maxc = max(maxc, count[char])
        
        return maxv+maxc


