class MedianFinder:

    def __init__(self):
        self.s=[] #smaller/left array 
        self.b=[] # bigger/right array

    def addNum(self, num: int) -> None:
        s=self.s
        b=self.b
        if(len(s)<len(b)):
            heapq.heappush(s,-num)
        else:
            heapq.heappush(b,num)
        if(len(s)>0 and len(b)>0 and -s[0]>b[0]):
            spop=-heapq.heappop(s)
            bpop=heapq.heappop(b)
            heapq.heappush(s,-bpop)
            heapq.heappush(b,spop)
        
        

    def findMedian(self) -> float:
        s=self.s
        b=self.b
        # print(s,b)
        if len(s) == len(b):
            return (-s[0]+b[0])/2
        elif(len(s)>len(b)):
            return -s[0]
        else:
            return b[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
