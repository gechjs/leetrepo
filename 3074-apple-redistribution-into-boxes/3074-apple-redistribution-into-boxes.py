class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        capacity.sort(reverse=True)

        ans = 0
        curr_capacity = 0
        total_apple = sum(apple)

        for val in capacity:
            curr_capacity+=val
            ans+=1
            if curr_capacity>=total_apple:
                break
        return ans