class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        # count = 0

        # left = 0
        # oddCount = 0
        # n = len(nums)
        # for right in range(len(nums)):
        #     if nums[right]%2 !=0 :
        #         oddCount+=1
            
        #     while oddCount==k:
        #         if nums[left]%2  != 0:
        #             oddCount-=1
        #         left+=1
            
        #     count += right-left+1
            
        
        # oddCount = 0
        # left = 0
        # for right in range(len(nums)):

        #     if nums[right]%2 !=0 :
        #         oddCount+=1
            
        #     while oddCount>k:
        #         count+=1
        #         if nums[left]%2  != 0:
        #             oddCount-=1
        #         left+=1
            
        # print(count)
        # return n*(n+1)//2 - count

        
        dic = Counter()

        count = 0
        ans = 0
        dic[0] = 1
        for i, num in enumerate(nums):
            count+= num%2
            ans += dic[count-k]
            dic[count]+=1
        return ans



