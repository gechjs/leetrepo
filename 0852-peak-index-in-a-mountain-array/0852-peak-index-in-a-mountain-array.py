class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left, right = 0, len(arr)-1

        while right>=left:
            mid = (right+left)//2
            
            if mid==0:
                mid = mid+1
            if mid== len(arr)-1:
                mid = len(arr)-1
            if arr[mid-1]>arr[mid]:
                right = mid-1
            elif arr[mid+1]>arr[mid]:
                left = mid+1
            else:
                return mid
        
        