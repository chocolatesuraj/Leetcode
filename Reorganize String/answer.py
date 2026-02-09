class Solution:
    def reorganizeString(self, s: str) -> str:
        chrs=[c for c in s]
        print(chrs)
        counts=Counter(s)
        heap=[]
        for c,count in counts.items():
            heapq.heappush(heap,(-count,c))
        ans=""
        while heap:
            ca,a=heapq.heappop(heap)
            ca=-ca
            if(not heap and ca>1):
                return ""
            elif(not heap and ca==1):
                ans+=a
                return ans 
            cb,b=heapq.heappop(heap)
            cb=-cb
            ans=ans+a+b
            if(ca-1>=1):
                heapq.heappush(heap,(-(ca-1),a))
            if(cb-1>=1):
                heapq.heappush(heap,(-(cb-1),b))
        return ans 
