class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        arr1 = version1.split(".")
        arr2 = version2.split(".")

        for i, char in enumerate(arr1):
            arr1[i]=int(char)
        for i, char in enumerate(arr2):
            arr2[i]=int(char)
        
        i = 0

        while i<len(arr1) and i<len(arr2):
            if arr1[i]>arr2[i]:
                return 1
            elif arr2[i]>arr1[i]:
                return -1
            
            i+=1
        
        while i < len(arr2):
            if arr2[i]>1:
                return -1
            i+=1
        while i < len(arr1):
            if arr1[i]>1:
                return 1
            i+=1
        return 0
        


            
        



