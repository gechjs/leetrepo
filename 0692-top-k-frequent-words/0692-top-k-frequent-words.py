class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)

        sorted_arr = sorted(count.items(), key = lambda x: x[0])
        sorted_arr = sorted(sorted_arr, key = lambda x: x[1], reverse= True)
        ans = []
        for i in range(k):
            ans.append(sorted_arr[i][0])
        return ans
