class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edges.sort()
        print(edges)
        arr=[i for i in range(n)]
        
        print(arr)
        comp=0 #component number
        
        arr[0]=0
        i=0
        while( comp<n):
            change=True
            while(change==True):
                i+=1
                # print(change,i)
                change=False
                for edge in edges:
                    # print("loop",arr,comp)
                    src,dst=edge
                    if arr[src]==comp and arr[dst]!=comp:
                        arr[dst]=arr[src]
                        change=True
                    if(arr[dst]==comp and arr[src]!=comp):
                        arr[src]=arr[dst]
                        change=True
            if(change==False):
                comp+=1
                change=True
        print("arr",arr)

        return len(set(arr))

