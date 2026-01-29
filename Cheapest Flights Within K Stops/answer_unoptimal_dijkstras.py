class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        hashmap=defaultdict(list)
        for s,d,c in flights:
            hashmap[s].append((d,c))
        heap=[] #airpot,cost up till there
        for d,c in hashmap[src]:
            heapq.heappush(heap,(c,0,d))
        while(heap):
            # print(heap)
            oldcost,jumps,s=heapq.heappop(heap)
            # print(oldcost,jumps,s)
            if(jumps>k):
                continue
            if(s==dst):
                return oldcost

            for d,c in hashmap[s]:
                heapq.heappush(heap,(c+oldcost,jumps+1,d))
        return -1
