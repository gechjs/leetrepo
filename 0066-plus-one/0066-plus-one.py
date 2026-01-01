class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = 1
        digit = digits[0]

        for val in digits[1:]:
            digit = digit*10+val

        digit+=1

        snum = str(digit)
        return [int(val) for val in snum]
