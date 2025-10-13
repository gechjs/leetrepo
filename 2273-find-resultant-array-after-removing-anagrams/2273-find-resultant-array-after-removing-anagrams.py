class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        curr = [Counter(words[0]), words[0]]

        i = 1
        if len(words) < 2:
            return words
            
        while i<len(words):
            while i< len(words) and Counter(words[i]) == curr[0]:
                i+=1
            ans.append(curr[1])
            
            if i < len(words):
                curr[0] = Counter(words[i])
                curr[1]= words[i]
            if i == len(words) -1 and Counter(words[i]) != Counter(words[i-1]):
                ans.append(words[-1])


            i+=1

        
        return ans