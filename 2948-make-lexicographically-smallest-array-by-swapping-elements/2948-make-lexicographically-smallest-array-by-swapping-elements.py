class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        copy = [(nums[i], i) for i in range(n)]

       
        copy.sort()
        
        left, right = 0, 1
        while right < n:
            pos = [copy[left][1]]
            while right < n and abs(copy[right][0] - copy[right - 1][0]) <= limit:
                pos.append(copy[right][1])
                right += 1

            pos.sort()
            for i in range(right - left):
                nums[pos[i]] = copy[left + i][0]

            left = right
            right += 1
        
        return nums
