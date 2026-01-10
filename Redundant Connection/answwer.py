class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.adj=defaultdict(set)
        for s,f in edges:
            self.adj[s].add(f)
            self.adj[f].add(s)
        # print(self.adj)
        
        for s,f in edges[::-1]:
            visited=[0]*(len(self.adj)+1)
            # print(s,self.adj[s],f)
            self.adj[s].remove(f)
            self.adj[f].remove(s)

            self.bfs(1,visited)
            # print(visited)
            flag=0
            for v in visited[1:]:
                if(v==0):
                    self.adj[s].add(f)
                    self.adj[f].add(s)
                    flag=1
                    break
            if(flag==0):
                return [s,f]

    def bfs(self,x,visited):
        visited[x]=1
        for node in self.adj[x]:

            if visited[node]==0:
                self.bfs(node,visited)




