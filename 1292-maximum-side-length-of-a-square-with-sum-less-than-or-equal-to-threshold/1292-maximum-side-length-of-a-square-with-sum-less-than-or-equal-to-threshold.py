class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        left, right = 0, min(len(mat), len(mat[0]))

        prefix = [[arr[i] for i in range(len(arr))] for arr in mat]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row-1>=0:
                    prefix[row][col]+=prefix[row-1][col]
                if col-1>=0:
                    prefix[row][col]+=prefix[row][col-1]
                if col-1>=0 and row-1>=0:
                    prefix[row][col]-=prefix[row-1][col-1]
        
        def check(num):
            for row in range(num-1, len(mat)):
                for col in range(num-1, len(mat[0])):
                    curr = prefix[row][col]

                    if row-num>=0:
                        curr-=prefix[row-num][col]
                    if col-num>=0:
                        curr-=prefix[row][col-num]
                    if col-num>=0 and row-num>=0:
                        curr+=prefix[row-num][col-num]
                    if curr<=threshold:
                        return True
            return False
                    
        
        while right>=left:
            mid = (right+left)//2

            if check(mid):
                left = mid+1
            else:
                right = mid-1
        
        return right