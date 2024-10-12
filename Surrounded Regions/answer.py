class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rl=len(board)
        cl=len(board[0])

        def spread(i,j):
            if(board[i][j]=="B"):
                return
            board[i][j]="B"
            print(i,j)
            if(i+1<rl and board[i+1][j]=="O"):
                board[i+1][j]=="B"
                spread(i+1,j)
            if(j+1<cl and board[i][j+1]=="O"):
                board[i][j+1]=="B"
                spread(i,j+1)
            if(i-1>=0 and board[i-1][j]=="O"):
                board[i-1][j]=="B"
                spread(i-1,j)
            if(j-1>=0 and board[i][j-1]=="O"):
                board[i][j-1]=="B"
                spread(i,j-1)
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                #print(i,j)
                if((i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1) and board[i][j]=="O"):
                    #print("test")
                    #board[i][j]="B"
                    spread(i,j)
        print(board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=="O"):
                    board[i][j]="X"
                elif(board[i][j]=="B"):
                    board[i][j]="O"
