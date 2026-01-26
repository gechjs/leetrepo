class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()

        ans = [[arr[0], arr[1]]]

        for i in range(2, len(arr)):
            diff = arr[i]-arr[i-1]
            curr = ans[0][1]-ans[0][0]
            if diff==curr:
                ans.append([arr[i-1], arr[i]])
            elif diff<curr:
                ans = [[arr[i], arr[i-1]]]
        return ans


       