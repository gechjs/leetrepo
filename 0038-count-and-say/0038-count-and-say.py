class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        num = "1"
        for _ in range(2, n + 1):
            res = []
            count = 1
            curr = num[0]
            for j in range(1, len(num)):
                if num[j] == curr:
                    count += 1
                else:
                    res.append(str(count) + curr)
                    curr = num[j]
                    count = 1
            res.append(str(count) + curr)
            num = "".join(res)
        return num