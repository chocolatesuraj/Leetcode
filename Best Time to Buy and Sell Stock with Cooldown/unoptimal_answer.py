class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices=prices
        self.memo = [[-1]*len(prices) for _ in range(len(prices))]
        # print(self.memo)
        return self.f(0,len(prices)-1)

    def f(self,s,f):
        # print(self.memo)
        # print("ip",s,f)
        
        if(s>f):
            return 0
        if(self.memo[s][f]!=-1):
            # print("check",s,f,self.memo[s][f])
            return self.memo[s][f]
        if(s==f):
            # print("eq",s,f)
            self.memo[s][f]=0
            return 0
        profit=self.prices[f]-self.prices[s]
        # print("prr",s,f,profit)

        if(f-s==1):
            # print("min case",s,f,profit)
            self.memo[s][f]=max(0,profit)
            # print("op min",s,f,profit)
            return max(0,profit)
        
        for i in range(s-1,f):
            # print("split point",i+1,"i+2=",i+2,"f",f)
            profit=max(profit,(self.f(s,i)+self.f(i+2,f)))
        # print("op",s,f,profit)
        self.memo[s][f]=max(0,profit)
        return max(0,profit)
