class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=set()
        columns=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    rows.add(i)
                    columns.add(j)
        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i]=0
        for col in columns:
            for i in range(len(matrix)):
                matrix[i][col]=0
        

        
