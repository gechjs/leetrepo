class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda  x:x[1])

        ans =[]
        for arr in intervals:
            if not ans:
                ans.append(arr[1]-1)
                ans.append(arr[1])
            else:
                if arr[0]>ans[-1]:
                    ans.append(arr[1]-1)
                    ans.append(arr[1])
                elif arr[0]==ans[-1]:
                    ans.append(arr[1])
                elif arr[0]<=ans[-2]:
                    continue
                else:
                    ans.append(arr[1])
        return len(ans)
                

                

