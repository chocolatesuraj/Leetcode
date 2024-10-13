class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # vis=[0 for _ in range(n)]
        # graph = [[0 for _ in range(n)] for _ in range(n)]
        # for edge in prerequisites:
        #     graph[edge[0]][egde[1]]=1
        n=numCourses
        vis=[[] for _ in range(n)]
        for edge in prerequisites:
            vis[edge[0]].append(edge[1])
        print(vis)
        for i in range(n):
            for arr in vis:
                for i in arr:
                    if(vis[i]==[]):
                        arr.remove(i)
        print(vis)
        for arr in vis:
            if arr!=[]:
                return False
        return True 


            
