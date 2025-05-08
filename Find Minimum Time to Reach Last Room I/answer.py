class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        minheap=[]
        heapq.heappush(minheap,[-1,(0,0),-1])
        moveTime[0][0] = -1 
        max_time=0
        while(minheap!=[]):
            # print(minheap)
            top=heapq.heappop(minheap)
            i,j=-top[1][0],-top[1][1]
            curtime=top[0]
            curtime=curtime+1
            # print(i,j,"  ",curtime)
            
            if(i==len(moveTime)-1 and j==len(moveTime[0])-1):
                return curtime
            if(i-1>=0 and moveTime[i-1][j]!=-1):
                heapq.heappush(minheap,[max(moveTime[i-1][j],curtime),(-i+1,-j)])
                moveTime[i-1][j]=-1
            if(i+1<len(moveTime) and moveTime[i+1][j]!=-1):
                heapq.heappush(minheap,[max(moveTime[i+1][j],curtime),(-i-1,-j)])
                moveTime[i+1][j]=-1
            if(j-1>=0 and moveTime[i][j-1]!=-1):
                heapq.heappush(minheap,[max(moveTime[i][j-1],curtime),(-i,-j+1)])
                moveTime[i][j-1]=-1
            if(j+1<len(moveTime[0]) and moveTime[i][j+1]!=-1):
                heapq.heappush(minheap,[max(moveTime[i][j+1],curtime),(-i,-j-1)])
                moveTime[i][j+1]=-1
                
        


        
