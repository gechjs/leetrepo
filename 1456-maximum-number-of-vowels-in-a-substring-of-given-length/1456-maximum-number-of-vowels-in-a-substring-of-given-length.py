class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        arr = ['a', 'e', 'i', 'o', 'u']
        vowel = set(arr)
        max_vowel= 0
        for i in range(k):
            if s[i] in vowel:
                max_vowel+=1
        curr = max_vowel
        for right in range(k, len(s)):
            if s[right] in vowel:
                curr+=1
            if s[right-k] in vowel:
                curr-=1
            max_vowel = max(max_vowel, curr)
        return max_vowel

