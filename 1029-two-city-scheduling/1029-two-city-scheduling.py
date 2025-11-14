class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        dic = {}


        for i, arr in enumerate(costs):
            dic[i]=arr[1]-arr[0]
        
        sorted_arr = sorted(dic.items(), key= lambda x:x[1])

        ans = 0

        for i, item in enumerate(sorted_arr):
            if i<len(sorted_arr)//2:
                ans+= costs[item[0]][1]
            else:
                ans+=costs[item[0]][0]
        return ans