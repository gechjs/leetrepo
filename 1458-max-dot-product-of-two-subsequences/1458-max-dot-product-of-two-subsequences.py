class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        def minElement(a):
            mn = a[0]
            for x in a[1:]:
                if x < mn:
                    mn = x
            return mn
        
        def maxElement(a):
            mx = a[0]
            for x in a[1:]:
                if x > mx:
                    mx = x
            return mx
        
        max1 = maxElement(nums1)
        max2 = maxElement(nums2)
        min1 = minElement(nums1)
        min2 = minElement(nums2)
        
       
        if max1 < 0 and min2 > 0:
            return max1 * min2
        if min1 > 0 and max2 < 0:
            return min1 * max2
        
        n, m = len(nums1), len(nums2)
        
        curr = [0] * (m + 1)
        nxt = [0] * (m + 1)
        
        for i in range(n - 1, -1, -1):
            curr, nxt = nxt, curr
            for j in range(m - 1, -1, -1):
                prod1 = nxt[j]                    
                prod2 = curr[j + 1]              
                prod3 = nums1[i] * nums2[j] + nxt[j + 1]  
                curr[j] = max(prod1, prod2, prod3)
        
        return curr[0]
