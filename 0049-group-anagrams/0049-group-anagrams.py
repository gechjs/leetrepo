class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []

        dic = defaultdict(list)
        empty_count = 0
        for word in strs:
            if not word:
                empty_count+=1
                continue
            dic[str(sorted(word))].append(word)  

        if empty_count:
            ans = [["" for _ in range(empty_count)]]

        for key, val in dic.items():
            ans.append(val)
        
        return ans