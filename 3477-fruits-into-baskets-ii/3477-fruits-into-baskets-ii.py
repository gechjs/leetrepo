class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        for i in range(len(fruits)):
            for j in range(i, len(fruits)):
                if fruits[i]<=baskets[j]:
                    baskets[j]=0
        
        return len(fruits) - baskets.count(0)
        

            