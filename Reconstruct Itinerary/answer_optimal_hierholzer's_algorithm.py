class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # counts={} # key= aiport value= [in,out]
        adj=defaultdict(list)
        for t in tickets:
            s,f =t[0],t[1]
            adj[s].append(f)
        for src,dsts in adj.items():
            dsts=dsts.sort(reverse=True) #sice we pop from back
        ans=[]
        def dfs(src):
            if adj[src]==[]:
                ans.append(src)
                return

            while(adj[src]!=[]):
                dst=adj[src].pop()
                dfs(dst)
                if adj[src]==[]:
                    ans.append(src)
                    return
        dfs("JFK")
        # print(ans)
        return ans[::-1]




                

        
        
