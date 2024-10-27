class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        valid=[1,2,3,4,5,6,7,8,9]
        for i in range(9):
            for j in range(9):
                if(board[i][j]!="."):
                    num=int(board[i][j])-1
                    if(valid[num]==100):
                        return False
                    valid[num]=100
            valid=[1,2,3,4,5,6,7,8,9]
        for i in range(9):
            for j in range(9):
                if(board[j][i]!="."):
                    num=int(board[j][i])-1
                    if(valid[num]==100):
                        return False
                    valid[num]=100
            valid=[1,2,3,4,5,6,7,8,9]

        for i in range(0,9,3):
            for j in range(0,9,3):
                for k in range (i,i+3):
                    for l in range(j,j+3):
                       if(board[k][l]!="."):
                            num=int(board[k][l])-1
                            if(valid[num]==100):
                                return False
                            valid[num]=100
                valid=[1,2,3,4,5,6,7,8,9]

                        



        

        return True
