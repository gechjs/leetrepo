class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        count = Counter()

        for arr in points:
            count[arr[1]]+=1
        
        ans = 0
        point = 0
        print(count)
        for key, val in count.items():
            if point==0:
                point+= val*(val-1)//2
            else:
                ans+=point*(val*(val-1)//2)
                point+=val*(val-1)//2
        return ans%(10**9 +7)