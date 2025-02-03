class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        loser = []
        for i in matches:
            loser.append(i[1])
        player = []
        for i in matches:
            player.append(i[0])
            player.append(i[1])

        count = Counter(player)
        setloser = set(loser)
        setplayer = set(player)
        loserdict = Counter(loser)
        
        curr = []
        for i in setplayer:
            if i not in setloser:
                curr.append(i)
        curr.sort()
        ans.append(curr)

        arr = []
        for key in loserdict:
            if loserdict[key]==1:
                arr.append(key)
        arr.sort()
        ans.append(arr)
        return ans


