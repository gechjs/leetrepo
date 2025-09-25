class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        

        dic = defaultdict(str)
        seen = set()
        arr = s.split()
        seen_word =set()

        for i, char in enumerate(pattern):
            if char not in seen:
                if arr[i] in seen_word:
                    return False
                dic[char]= arr[i]
                seen.add(char)
                seen_word.add(arr[i])
            else:
                if dic[char] != arr[i]:
                    return False
        
        return len(pattern) == len(arr) 