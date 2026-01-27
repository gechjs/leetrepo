class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row_fre = Counter(board[i])
            for key in row_fre:
                if row_fre[key]>1 and key != ".":
                    print("row")
                    return False
        for i in range(9):
            col_fre = Counter()
            for j in range(9):
                col_fre[board[j][i]]+=1
            for key in col_fre:
                if col_fre[key]>1 and key !=".":
                    print("col")
                    return False
        i=0
        while i<9:
            j=0
            count = Counter()
            while j<9:
                count.clear()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        count[board[l][k]]+=1
                    
                for key in count:
                    if count[key]>1 and key !=".":
                        print(count)
                        print(i)
                        print(j)
                        print("spr")
                        return False
                

                j+=3
            i+=3
        return True




