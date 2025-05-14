MOD = 10**9 + 7

class Solution:
    def matrix_multiplication(self, A, B):
        res = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
        return res
    
    def matrix_exponentiation(self, transformation_matrix, t):
        res = [[0] * 26 for _ in range(26)]
       
        for i in range(26):
            res[i][i] = 1
        
        while t > 0:
            if t & 1:
                res = self.matrix_multiplication(transformation_matrix, res)
            transformation_matrix = self.matrix_multiplication(transformation_matrix, transformation_matrix)
            t >>= 1
        return res
    
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        initial_freq = [0] * 26
        for c in s:
            initial_freq[ord(c) - ord('a')] += 1
        
        transformation_matrix = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(i + 1, i + nums[i] + 1):
                transformation_matrix[j % 26][i] += 1
        
        res = self.matrix_exponentiation(transformation_matrix, t)
        final_array = [0] * 26
        for i in range(26):
            for j in range(26):
                final_array[i] = (final_array[i] + res[i][j] * initial_freq[j]) % MOD
        
        string_size = sum(final_array) % MOD
        return string_size