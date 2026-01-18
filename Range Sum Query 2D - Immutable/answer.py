class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        presum=[[0]*len(matrix[0]) for i in range(len(matrix))]
        s=0
        for i in range(len(matrix)):
            temp=0
            for j in range(len(matrix[0])):
                if(i==0): # first row 
                    temp+=matrix[i][j]
                    presum[i][j]=temp
                else:
                    temp=temp+matrix[i][j]
                    presum[i][j]=temp+presum[i-1][j]
        # print (presum)
        self.presum=presum


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=self.presum[row2][col2]
        # print(ans,self.presum[row1-1][col2],self.presum[row2][col1-1])
        if(row1-1>=0):
            ans=ans-self.presum[row1-1][col2]
        if(col1-1>=0):
            ans=ans-self.presum[row2][col1-1]
        if(col1-1>=0 and row1-1>=0):
            ans+=self.presum[row1-1][col1-1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
