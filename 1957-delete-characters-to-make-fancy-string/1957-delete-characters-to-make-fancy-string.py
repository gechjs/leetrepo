class Solution:
    def makeFancyString(self, s: str) -> str:
        arr = []
        count = 1
        for char in s:
            if arr and char == arr[-1]:
                count +=1 
                if count <= 2:
                    arr.append(char)
            else:
                count = 1
                arr.append(char)
        return "".join(arr)