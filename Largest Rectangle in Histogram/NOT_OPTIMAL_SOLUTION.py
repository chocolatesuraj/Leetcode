class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  
        self.ans=0
        self.h=heights 
        for i in range(len(self.h)):
            # print(i,i)
            self.sol(i,i,1,self.h[i])
        return self.ans

    def sol(self,l,r,lenght,mini):
        # print(l,r,lenght,mini)
        if(len(self.h)*mini<self.ans):
            return 
        if(lenght*mini>self.ans):
            self.ans=lenght*mini
        if(r+1<len(self.h)):
            rmini=mini
            if(self.h[r+1]<mini):
                rmini=self.h[r+1]
            self.sol(l,r+1,lenght+1,rmini)
        if(l-1>=0):
            lmini=mini
            if(self.h[l-1]<mini):
                lmini=self.h[l-1]
            self.sol(l-1,r,lenght+1,lmini)
        
