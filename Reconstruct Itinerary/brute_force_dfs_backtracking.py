class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        t_dict=defaultdict(int) # tickets dictionary to track used tickets 
        total=len(tickets)
        for t in tickets:
            s,f =t[0],t[1]
            adj[s].append(f)
            t_dict[(s,f)]+=1

        # sort for lexicologial answer 
        for src,destinations in adj.items():
            destinations.sort()
            

        # print(adj)
        def dfs(src):
            nonlocal total
            nonlocal ans
            if(total==0):
                return True
            for dst in adj[src]:
                # print(src,dst)
                if(t_dict[(src,dst)]>0):
                    t_dict[(src,dst)]-=1
                    ans.append(dst)
                    total-=1
                    op=dfs(dst)
                    if op:
                        return ans
                    ans.pop()
                    total+=1
                    t_dict[(src,dst)]+=1
            return False 

        ans=["JFK"]
        return dfs("JFK")


                

        
        
