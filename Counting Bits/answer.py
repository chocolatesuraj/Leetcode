class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[-1]*(n+1)
        prev=2 # pointer to see how many positions back to look
        for i in range(0,n+1):
            # print(i,prev)
            if(i==prev):
                prev=prev*2
                
            if(i==0):
                dp[i]=0
            elif(i==1):
                dp[i]=1
            else:
                dp[i]=dp[i-int(prev/2)]+1
        return dp
                
                
