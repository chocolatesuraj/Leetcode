class Node():
    def __init__(self,val):
        self.val=val
        self.n={}
        self.time=-1
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodemap={}
        for i in range(1,n+1):
            nodemap[i]=Node(i)
        for time in times:
            src,dest,t=time[0],time[1],time[2]
            nodemap[src].n[dest]=t
        # print(nodemap)
        self.nodemap=nodemap
        self.bfs(k,0)
        #graph has now been constructed
        max_time=0
        for key,node in self.nodemap.items():
            if node.time==-1:
                return -1
            elif node.time>max_time:
                max_time=node.time
        return max_time
            

    def bfs(self,k,dist):
        if self.nodemap[k].time!=-1 and  self.nodemap[k].time<=dist:
            return 
        self.nodemap[k].time=dist
        for key,value in self.nodemap[k].n.items():
            self.bfs(key,value+dist)

    





