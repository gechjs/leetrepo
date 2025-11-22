class Solution:
    def minimumFlips(self, n: int) -> int:
        
        bits =bin(n)[2:]
        arr = []
        for i in range(len(bits)-1, -1, -1):
            arr.append(bits[i])
       
        ans = 0
       
        for i in range(len(bits)):
            if bits[i] != arr[i]:
                ans+=1
        return ans