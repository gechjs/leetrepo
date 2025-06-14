class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        stringnum = str(num)
        large = 9
        small = 0
        for digit in stringnum:
            if digit != "9":
                large = digit
                break
            
        for digit in stringnum:
            if digit != "0":
                small = digit
                break
        
        maxval = ''
        minval = ''
        for digit in stringnum:
            if digit == large:
                maxval += '9'
            else:
                maxval += digit
            
            if digit == small:
                minval+= "0"
            else:
                minval += digit
        return int(maxval)-int(minval)