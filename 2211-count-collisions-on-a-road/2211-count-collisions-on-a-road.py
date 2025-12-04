class Solution:
    def countCollisions(self, directions: str) -> int:
        
        stack = []
        ans = 0
        for char in directions:
            if not stack:
                stack.append(char)
            else:
                if char == "R":
                    stack.append(char)
                elif char== "L":
                    if stack[-1]== "R":
                        ans+=2
                        stack.pop()
                        while stack and stack[-1]== "R":
                            ans+=1
                            stack.pop()
                        stack.append("S")
                    elif stack[-1]== "S":
                        ans+=1
                else:
                    while stack and stack[-1]== "R":
                        ans+=1
                        stack.pop()
                    stack.append("S")
        return ans
        