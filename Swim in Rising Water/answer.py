class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap=[]
        heapq.heappush(heap,(grid[0][0],0,0))
        while(heap!=[]):
            height,i,j=heapq.heappop(heap)
            if(grid[i][j]==-1):
                continue
            else:
                grid[i][j]=-1
            if(i==len(grid)-1 and j==len(grid)-1):
                return max(height,grid[i][j])

            if(i-1>=0):
                heapq.heappush(heap,( max(height,grid[i-1][j]), i-1, j ))
            if(i+1<len(grid)):
                heapq.heappush(heap,(max(height,grid[i+1][j]),i+1,j))
            if(j-1>=0):
                heapq.heappush(heap,(max(height,grid[i][j-1]),i,j-1))
            if(j+1<len(grid)):
                heapq.heappush(heap,(max(height,grid[i][j+1]),i,j+1))

            

