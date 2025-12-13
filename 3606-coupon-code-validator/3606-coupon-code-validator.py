class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        dic = defaultdict(list)
        myset = set(["electronics", "grocery", "pharmacy", "restaurant"])
        for i in range(len(code)):
            flag = True
            for char in code[i]:
                if not char.isalnum() and char != "_":
                    flag = False
                    break
            if flag:
                if code[i] and isActive[i] and businessLine[i] in myset:
                    dic[businessLine[i]].append(code[i]) 
        
        
        ans = sorted(dic['electronics'])+sorted(dic["grocery"])+sorted(dic["pharmacy"])+sorted(dic["restaurant"])
        
        return ans

