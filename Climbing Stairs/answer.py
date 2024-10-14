class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonacci series
        prev1=1
        prev2=2
        res=0
        if(n==1):
            return 1
        if(n==2):
            return 2
        for i in range(n-2):
            res=prev2+prev1
            prev1=prev2
            prev2= res
        return res
            
            
        
