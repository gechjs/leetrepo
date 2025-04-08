class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and j!=k and i != k:
                        num = digits[i]*100+digits[j]*10 + digits[k]
                        if num % 2 == 0 and num >= 100:
                            ans.add(num)
        
        return len(ans)
