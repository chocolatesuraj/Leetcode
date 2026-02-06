class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.q=[None]*k
        self.f,self.b=0,-1
        self.l=0
        

    def enQueue(self, value: int) -> bool:
        # print(value)
        # print(self.q,self.f,self.b)
        if(self.b<self.k-1 and self.q[self.b+1]==None):
            self.b+=1
            self.q[self.b]=value
            self.l+=1
            return True
        
        elif(self.b==self.k-1 and self.q[0]==None):
            self.b=0
            self.q[0]=value
            self.l+=1
            return True 
        return False
            

    def deQueue(self) -> bool:
        # print("deque")
        # print(self.q,self.f,self.b)
        if self.q[self.f]!=None:
            self.l-=1
            self.q[self.f]=None
            self.f+=1
            if(self.f==self.k):
                self.f=0
            return True
        return False

    def Front(self) -> int:
        if self.q[self.f]!=None:
            return self.q[self.f]
        return -1
        

    def Rear(self) -> int:
        if self.q[self.b]!=None:
            return self.q[self.b]
        return -1
        

    def isEmpty(self) -> bool:
        if self.l==0:
            return True 
        return False
        

    def isFull(self) -> bool:
        if self.l==self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
