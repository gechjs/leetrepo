class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        length = len(tops)

        dic = defaultdict(set)

        for i, val in enumerate(tops):
            dic[i].add(val)
        for i, val in enumerate(bottoms):
            dic[i].add(val)
        
        count = Counter()
        for char in dic:
            for num in dic[char]:
                count[num]+=1
        for num in count:
            if count[num]==length:
                break
        else:
            return -1
        

        top = Counter(tops)
        bottom = Counter(bottoms)

        t_val = max(list(top.values()))
        b_val = max(list(bottom.values()))

        return min(length-t_val, length-b_val)
        
