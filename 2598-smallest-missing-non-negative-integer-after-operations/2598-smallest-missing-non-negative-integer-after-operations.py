class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        
        myset = set()
        arr = []
        count = Counter(nums)
        newcount = Counter()
        for num, val in count.items():
            if num<0 and num%value!=0:
                newnum = -1*num
                newcount[value - newnum%value]+= count[num]   
            else:
                newcount[num%value]+=count[num]
        print()
        for key, val in newcount.items():
            tobeadd = key
            for i in range(val):
                while tobeadd in myset:
                    tobeadd+=value
                myset.add(tobeadd)
                if tobeadd > len(nums):
                    break
        
        for i in range(max(myset)+1):
            if i not in myset:
                return i
        return i+1
        



