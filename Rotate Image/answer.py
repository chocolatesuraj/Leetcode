class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        n=len(matrix)-1
        for i in range (0,len(matrix)):
            for j in range(0,len(matrix)-i):
                temp=matrix[i][j]
                matrix[i][j]=matrix[n-j][n-i]
                matrix[n-j][n-i]=temp
                # print(i,j,matrix[i][j],matrix[j][i])
        # print("aa",n+1)
        # print(int((n+1)/2))
        # print(matrix)
        for i in range(0,int((n+1)/2)):
            temp= matrix[i]
            matrix[i]=matrix[n-i]
            matrix[n-i]=temp

        # print(matrix)
