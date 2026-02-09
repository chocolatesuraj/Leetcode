class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        # print(price,self.stack)
        if not self.stack:
            self.stack.append((price,1))
            return 1
        if(price<self.stack[-1][0]):
            self.stack.append((price,1))
            return 1
        count=1
        while(self.stack and self.stack[-1][0]<=price):
            ele,c=self.stack.pop()
            count=count+c
        self.stack.append((price,count))
        return count


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
