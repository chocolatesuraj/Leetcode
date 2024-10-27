class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones)==1):
            return stones[0]

        minHeap= [-x for x in stones] 
        heapq.heapify(minHeap) 
        while (len(minHeap)>1):
            print(minHeap)
            a=-heapq.heappop(minHeap)
            b=-heapq.heappop(minHeap)
            print(a,b)
            if(a>b):
                heapq.heappush(minHeap, b-a)
            elif(a<b):
                heapq.heappush(minHeap, a-b)
        print(minHeap)
        if(len(minHeap)>0):
            return -minHeap[0]
        return 0
