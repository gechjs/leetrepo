from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        ans = set() 

        for i in range(len(digits)):
            if digits[i] == 0:
                continue  
            for j in range(len(digits)):
                if j == i:
                    continue
                for k in range(len(digits)):
                    if k == i or k == j:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0:
                        ans.add(num)

        return sorted(ans)
