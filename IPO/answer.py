class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap=[]
        pairs=[]
        
        for i in range(len(profits)):
            pairs.append([capital[i],profits[i]])
        pairs.sort(reverse=True)
        # print(pairs)

        count=0
        currprof=w
        
        while(count<k):
            while(pairs and pairs[-1][0]<=currprof):
                cap,prof=pairs.pop()
                heapq.heappush(heap,-prof)
            # print("heap",heap,count)
            if heap:
                prof=heapq.heappop(heap)
                # print("pop",prof)
            else:
                # print("return")
                return currprof
            currprof+=-prof
            count+=1
        return currprof

