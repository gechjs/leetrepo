
class Solution:
    def hasSameDigits(self, word: str) -> bool:
        
        while len(word) != 2:
             newstr = ''
             for i in range(1, len(word)):  
                digit = int(word[i])+int(word[i-1]) 
                digit = digit%10
                newstr+=str(digit)
             word = newstr
        return True if word[0]==word[1] else False