class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.l=len(matrix)
        self.b=len(matrix[0])
        self.nums=matrix
        ans=0
        self.memo=[[-1]*self.b for i in range(self.l)]
        for i in range (self.l):
            for j in range (self.b):
                a=1+self.f(i,j)
                ans=max(ans,a)
        return ans 
    def f(self,x,y):
        a,b,c,d=0,0,0,0
        if(self.memo[x][y]!=-1):
            return self.memo[x][y]
        if(x+1<self.l and self.nums[x+1][y]>self.nums[x][y]):
            a=1+self.f(x+1,y)
        if(x-1>=0 and self.nums[x-1][y]>self.nums[x][y]):
            b=1+self.f(x-1,y)
        if(y+1<self.b and self.nums[x][y+1]>self.nums[x][y]):
            c=1+self.f(x,y+1)
        if(y-1>=0 and self.nums[x][y-1]>self.nums[x][y]):
            d=1+self.f(x,y-1)
        self.memo[x][y]=max(a,b,c,d)
        return max(a,b,c,d)
        
