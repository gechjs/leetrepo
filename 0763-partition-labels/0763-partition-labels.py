class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dic = {char: index for index, char in enumerate(s)}
        ans = []
        length, end = 0, 0
        for inx, char in enumerate(s):
            length+=1
            end = max(end, dic[char])

            if inx==end:
                ans.append(length)
                length = 0
        return ans


