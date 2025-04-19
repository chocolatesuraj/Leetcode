class Node():
    def __init__(self,val):
        self.val=val
        self.n={}
        self.visited=-1
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodemap={}
        for i in range(1,n+1):
            nodemap[i]=Node(i)
        for time in times:
            src,dest,t=time[0],time[1],time[2]
            nodemap[src].n[dest]=t
        # print(nodemap)
        #graph has now been constructed

        max_time=0

        minheap=[]
        heapq.heappush(minheap,[0,k])
        # nodemap[k].visited=1
        while(minheap!=[]):
            dist,k=heapq.heappop(minheap)
            if(nodemap[k].visited==1):
                continue 
            nodemap[k].visited=1
            # print("popped",dist,k)
            if(dist>max_time):
                max_time=dist
            nodemap[k].visited=1
            for key,value in nodemap[k].n.items():
                # print("loop")
                if(nodemap[key].visited==-1):
                    # print("insert",dist+value,key)
                    heapq.heappush(minheap,[dist+value,key])



        for key,node in nodemap.items():
            if node.visited==-1:
                return -1
        return max_time
            

    





