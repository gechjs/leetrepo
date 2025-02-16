class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        
        pizzas.sort()

        days = len(pizzas)//4
        n = int(days*4)-1
        flag = True
        ans = 0
        right=0
        left=1
        jamp= days//2 if days%2==0 else days//2+1
        print(pizzas)
        for _ in range(days):
            if flag:
                ans+=pizzas[n-right]
                right+=1
                flag=False
            else:
                ans+=pizzas[n-left-jamp]
                left+=2
                flag = True
        return ans