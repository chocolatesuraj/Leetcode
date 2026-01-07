class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.ans=0
        self.prices=prices
        self.memo=[[-1]*len(prices) for i in range(2)]
        print(self.memo)
        return self.f(0,1)
        
    def f(self,pos,state): #state=1 -> can buy state=0 -> bought, can sell 
        # print(pos,state)
        if(pos>=len(self.prices)):
            return 0
        if(self.memo[state][pos]!=-1):
            return self.memo[state][pos]
        if(state==1):
            #buy
            a=self.f(pos+1,0) - self.prices[pos]
            #dont buy
            b=self.f(pos+1,1)
            self.memo[state][pos]=max(a,b)
            return max(a,b)
        if(state==0):
            #sell
            a=self.f(pos+2,1) +self.prices[pos]
            #hold
            b=self.f(pos+1,0)
            self.memo[state][pos]=max(a,b)
            return max(a,b)
        
