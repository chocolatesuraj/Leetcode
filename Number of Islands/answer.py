class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid=grid
        def check_for_x(grid, i, j):
            #print(grid,i,j)
            rows = len(grid)
            cols = len(grid[0])
            val=False
            if i + 1 < rows and self.grid[i+1][j] == "x":
                val=True
                #print('ifff')
            elif i + 1 < rows and self.grid[i+1][j] == "1":
                self.grid[i+1][j] = "x"
                #print('ellllllllifff')
                x=check_for_x(grid, i+1, j)

            if i - 1 >= 0 and self.grid[i-1][j] == "x":
                val=True
            elif i - 1 >= 0 and self.grid[i-1][j] == "1":
                grid[i-1][j] = "x"
                x=check_for_x(grid, i-1, j)

            if j + 1 < cols and self.grid[i][j+1] == "x":
                val=True
            elif j + 1 < cols and self.grid[i][j+1] == "1":
                grid[i][j+1] = "x"
                x=check_for_x(grid, i, j+1)

            if j - 1 >= 0 and grid[i][j-1] == "x":  # Changed j-j to j-1 (assuming this was a typo)
                val=True
            elif j - 1 >= 0 and self.grid[i][j-1] == "1":
                grid[i][j-1] = "x"
                x=check_for_x(grid, i, j-1)

            return val

        nums=0
        print(len(grid))
        print(len(grid[0]))

        for i  in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if(self.grid[i][j]=="0"):
                    continue
                elif(self.grid[i][j]=="1"):
                    nums=nums+1
                    if (check_for_x(self.grid, i, j)):
                        self.grid[i][j]="x"
                    else:
                        self.grid[i][j]="x"
                        #nums=nums+1
                #print(self.grid)
                #print(i,j,nums)
            
        return nums


        
