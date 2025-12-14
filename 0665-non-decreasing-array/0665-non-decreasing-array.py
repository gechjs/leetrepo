class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        stack = [nums[0]]
        count = 0
        for i in range(1, len(nums)):
            if nums[i]>=stack[-1]:
                stack.append(nums[i])
            else:
                if len(stack)==1:
                    stack[-1]= -1*10**5
                    stack.append(nums[i])
                    count+=1
                else:
                    if nums[i]>=stack[-2]:
                        stack[-1]=stack[-2]
                        count+=1
                        stack.append(nums[i])
                    else:
                        count+=1
                        stack.append(stack[-1])
            if count>1:
                break
        return count<=1