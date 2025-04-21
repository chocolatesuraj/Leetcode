class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.grid = [[-1 for _ in range(n)] for _ in range(m)]        
        self.bfs(m-1,n-1)
        # print(self.grid)
        return self.grid[m-1][n-1]

    def bfs(self,i,j):
        # print(i,j)
        top=0
        back=0
        if(i==0 and j==0):
            self.grid[i][j]=1
            return 

        if(j-1>=0):
            if(self.grid[i][j-1]==-1):
                self.bfs(i,j-1)
            top=self.grid[i][j-1]
        if(i-1>=0):
            if(self.grid[i-1][j]==-1):
                self.bfs(i-1,j)
            back=self.grid[i-1][j]

        # print(i,j,"  ",top,back)
        val=top+back
        
        self.grid[i][j]=val
        # return val 
    
