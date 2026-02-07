class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[-1]*n
        prices[src]=0
        for i  in range (k+1):
            newprices=prices[:]
            for s,d,price in flights:
                if(prices[s]!=-1):
                    cost=prices[s]+price
                    if(cost<newprices[d] or newprices[d]==-1 ):
                        newprices[d]=cost
            if(newprices==prices):
                return prices[dst]
            prices=newprices
        return prices[dst]
                    


                
