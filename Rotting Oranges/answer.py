class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.mins=2
        self.grid=grid

        def rot(i, j):
            rows = len(self.grid)
            cols = len(self.grid[0])

            if i + 1 < rows and self.grid[i+1][j] == 1:
                self.grid[i+1][j]=self.mins+1

            if i - 1 >= 0 and self.grid[i-1][j] == 1:
                self.grid[i-1][j]=self.mins+1

            if j + 1 < cols and self.grid[i][j+1] == 1:
                self.grid[i][j+1]=self.mins+1

            if j - 1 >= 0 and self.grid[i][j-1] == 1:  
                self.grid[i][j-1]=self.mins+1
        maxx=0
        rows = len(self.grid)
        cols = len(self.grid[0])
        if rows>cols:
            maxx=rows
        else:
            maxx=cols
        maxx=2*maxx
        print(maxx)
        cont=False
        for i  in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if self.grid[i][j]==1:
                        cont=True
        if(cont==False):
            return 0
        cont=False
        for w in range(rows*cols):
            print(self.grid)
            if(cont==True):
                self.mins=self.mins+1
            cont=False

            for i  in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if self.grid[i][j]==self.mins:
                        rot(i,j)
            for i  in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if self.grid[i][j]==1:
                        cont=True

        if(cont==True):
            return -1
        return self.mins+1-2 


        
