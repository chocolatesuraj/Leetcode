class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        w=len(heights[0])
        h=len(heights)
        def flow(height,i,j,pa):
            #print(i,j,pa)
            if(i-1>=0 and ((i-1,j) not in pa ) ):
                
                if(heights[i-1][j]>=height):
                    pa.add((i-1,j))
                    flow(heights[i-1][j],i-1,j,pa)
            if(j-1>=0 and ((i,j-1) not in pa ) ):
                
                if(heights[i][j-1]>=height):
                    pa.add((i,j-1))
                    flow(heights[i][j-1],i,j-1,pa)
            if(j+1<w and ((i,j+1) not in pa ) ):
                
                if(heights[i][j+1]>=height):
                    pa.add((i,j+1))
                    flow(heights[i][j+1],i,j+1,pa)
            if(i+1<h and ((i+1,j) not in pa ) ):
                #pa.add((i+1,j))
                if(heights[i+1][j]>=height):
                    pa.add((i+1,j))
                    flow(heights[i+1][j],i+1,j,pa)

        w=len(heights[0])
        h=len(heights)
        p=set()
        a=set()
        for i in range(w):
            p.add((0,i))
        for i in range(h):
            p.add((i,0))
        for i in range(w):
            a.add((h-1,i))
        for i in range(h):
            a.add((i,w-1))
        visitedp=set()
        pv=p.copy()
        av=a.copy()
        for ele in p:
            i,j=ele
            height=heights[i][j]
            flow(height,i,j,pv)
        for ele in a:
            i,j=ele
            height=heights[i][j]
            flow(height,i,j,av)

        result = av.intersection(pv)
        print(pv,"xxxxxxxx",av)
        #print (result)
        ans=[[i,j] for (i,j) in result ]
        return ans
            

        



