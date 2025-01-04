class Solution:
    def __init__(self):
        self.solnmap={}
    def myPow(self, x: float, n: int) -> float:
        #print(n)
        if(n==1):
            return x
        if(n==0):
            return 1
        if(n==-1):
            return 1/x
        else:
            if(n in self.solnmap):
                return self.solnmap[n]
            else:
                #print(n)
                half=int(n/2)
                #print(half,n-half)
                ans=self.myPow(x,half)*self.myPow(x,n-half)
                self.solnmap[n]=ans
                return ans
        
