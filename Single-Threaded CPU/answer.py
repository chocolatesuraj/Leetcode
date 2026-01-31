class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap=[]
        ans=[]
        tasks=[[tasks[i][0],tasks[i][1],i] for i in range(len(tasks))]
        tasks.sort(key= lambda x:x[0])
        currtime=0
        i=0
        while i<len(tasks) or heap!=[]:
            
            while(i<len(tasks) and tasks[i][0]<=currtime):
                heapq.heappush(heap,(tasks[i][1],tasks[i][2]))#processing time,index
                i+=1
            if not heap:
                currtime=tasks[i][0]
            # print(heap,currtime)
            if heap:
                task_time,index=heapq.heappop(heap)
                currtime=currtime+task_time
                ans.append(index)
        return ans



