class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)

        arr = list(count.values())
        arr.sort()
        odd = 0
        even = 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i] & 1:
                odd = arr[i]
                break
        for val in arr:
             if not val & 1:
                even = val
                break
        return odd - even