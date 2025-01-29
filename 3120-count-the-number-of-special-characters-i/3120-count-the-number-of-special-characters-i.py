class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        myset = set(word)
        count = 0

        seen = set()

        for i in myset:
            if i.swapcase() in seen:
                count+=1
                seen.remove(i.swapcase())
            else:
                seen.add(i)
        return count

