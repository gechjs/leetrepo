class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):

            str_num = str(num)
            if len(str_num)%2:
                continue
            left = 0
            right = 0
            for i in range(len(str_num)):
                if i<len(str_num)//2:
                    left+=int(str_num[i])
                else:
                    right+=int(str_num[i])
            if right == left:
                count+=1
        return count