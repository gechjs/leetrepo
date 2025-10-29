class Solution:
    def smallestNumber(self, n: int) -> int:
        
        bits = bin(n)[2:]
        arr = []
       
        for bit in bits:
            if bit == "1":
                arr.append("1")
                continue
            
            arr.append("1")
        
        return int("".join(arr), 2)