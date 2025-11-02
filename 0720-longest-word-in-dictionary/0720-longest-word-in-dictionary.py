class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        dic = defaultdict(list)
        myset = set(words)
        for word in words:
            for i in range(len(word)+1):
                if i == len(word):
                    dic[len(word)].append(word)

                if word[:i+1] not in myset:
                    break
        if not dic:
            return ''
        maxval = max(dic)
        print(dic[maxval])
        return sorted(dic[maxval])[0]
