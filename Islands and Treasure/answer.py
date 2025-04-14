class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid=grid
        print(grid)
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    self.bfs(i,j,0) 
    def bfs(self,i,j,dist):
        print(i,j,dist,self.grid[i][j])
        if(self.grid[i][j]==-1 ): # cant traverse water 
            return 
        if(dist > self.grid[i][j]): # shorter path already preesent 
            return 
        if(dist<=self.grid[i][j] and dist!=0): #shorter distance found, Update 
            self.grid[i][j]=dist
        
        
        print("rec")
        if(i+1<len(self.grid)):
            self.bfs(i+1,j,dist+1)
        if(j+1<len(self.grid[0])):
            self.bfs(i,j+1,dist+1)
        if(i-1>=0):
            self.bfs(i-1,j,dist+1)
        if(j-1>=0):
            self.bfs(i,j-1,dist+1)




        
