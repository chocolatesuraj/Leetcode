class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        memo={}
        ans=float("inf")
        hashmap=defaultdict(list)
        for s,d,c in flights:
            hashmap[s].append((d,c))
        heap=[] #airpot,cost up till there
        while hashmap[src]:
            d,c =hashmap[src].pop()
            heapq.heappush(heap,(0,c,d))
        while(heap):
            # print(heap)
            jumps,oldcost,s=heapq.heappop(heap)
            # print(oldcost,jumps,s)
            
            if(jumps>k):
                break
            if(s==dst):
                if(oldcost<ans):
                    ans=oldcost
            
            for d,c in  hashmap[s]:
                if(jumps+1<=k):
                    if(d not in memo or (memo[d][0]>jumps+1 or memo[d][1]>c+oldcost )):
                        heapq.heappush(heap,(jumps+1,c+oldcost,d))
                        memo[d]=[jumps+1,oldcost+c]
        if(ans==float("inf")):
            return -1
        return ans
            

