class Solution:
    def countPoints(self, rings: str) -> int:
        
        dic = defaultdict(set)

        for i in range(0, len(rings), 2):
            dic[rings[i+1]].add(rings[i])

        ans = [len(item) for item in dic.values()]

        count = Counter(ans)
        print(ans, dic)
        return count[3]
