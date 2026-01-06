class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1, arr2):
            right, left = 0, 0
            arr = []
            while right<len(arr1) and left<len(arr2):
                if arr1[right]<arr2[left]:
                    arr.append(arr1[right])
                    right+=1
                else:
                    arr.append(arr2[left])
                    left+=1
            while left<len(arr2):
                arr.append(arr2[left])
                left+=1
            while right<len(arr1):
                arr.append(arr1[right])
                right+=1
            return arr
      
        def fun(arr):
            mid = len(arr)//2
            if len(arr) <=1:
                return arr
            l = fun(arr[:mid])
            r = fun(arr[mid:])
            sorted_arr = merge(l, r)
            return sorted_arr
        return fun(nums)

