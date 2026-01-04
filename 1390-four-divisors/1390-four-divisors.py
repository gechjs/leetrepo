class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        ans = 0

        for num in nums:
            # cnt = 0
            # _sum = 0
            seen = set()
            for i in range(2, int(sqrt(num))+1):
                if num%i == 0:
                    # cnt+=1
                    # _sum=i+num//i
                    seen.add(i)
                    seen.add(num//i)
                if len(seen)>2:
                    break
            if len(seen)==2:
                # ans+=1+_sum+num
                ans+=sum(seen)+1+num
                
        return ans


        
        