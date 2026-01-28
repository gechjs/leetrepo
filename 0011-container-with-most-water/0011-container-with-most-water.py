class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        j = len(height)-1
        i=0
        while j>i:
            area = (j-i)*min(height[j], height[i])
            max_area = max(max_area, area)
            if height[j] > height[i]:
                i+=1
            else:
                j-=1
        return max_area