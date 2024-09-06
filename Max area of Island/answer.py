class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid=grid
        self.count=0
        def check_for_x(grid, i, j):
            #print(grid,"\n",i,j,self.count)
            rows = len(grid)
            cols = len(grid[0])
            val=False
            if i + 1 < rows and self.grid[i+1][j] == 999:
                val=True
                #print('ifff')
            elif i + 1 < rows and self.grid[i+1][j] == 1:
                self.grid[i+1][j] = 999
                self.count=self.count+1
                #print('ellllllllifff')
                x=check_for_x(grid, i+1, j)

            if i - 1 >= 0 and self.grid[i-1][j] == 999:
                val=True
            elif i - 1 >= 0 and self.grid[i-1][j] == 1:
                grid[i-1][j] = 999
                self.count=self.count+1
                x=check_for_x(grid, i-1, j)

            if j + 1 < cols and self.grid[i][j+1] == 999:
                val=True
            elif j + 1 < cols and self.grid[i][j+1] == 1:
                grid[i][j+1] = 999
                self.count=self.count+1
                x=check_for_x(grid, i, j+1)

            if j - 1 >= 0 and grid[i][j-1] == 999:  # Changed j-j to j-1 (assuming this was a typo)
                val=True
            elif j - 1 >= 0 and self.grid[i][j-1] == 1:
                grid[i][j-1] = 999
                self.count=self.count+1
                x=check_for_x(grid, i, j-1)
            #print(grid,"\n",i,j,self.count)
            return self.count

        nums=0
        print(len(grid))
        print(len(grid[0]))
        max=0
        for i  in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if(self.grid[i][j]==0):
                    continue
                elif(self.grid[i][j]==1):
                    self.count=1
                    self.grid[i][j]=999
                    check_for_x(self.grid, i, j)
                    if max<self.count:
                        max=self.count
                        self.count=0
                    
                        #nums=nums+1
                #print(self.grid)
                #print(i,j,max)
            
        return max
        
