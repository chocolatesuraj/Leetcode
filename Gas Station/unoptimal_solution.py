class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net=[]
        for i  in range(0,len(gas)):
            # print(i)
            net.append(gas[i]-cost[i])
        
        # print(net)
        visited=[0]* len(net) # indexed that are started from 

        start=0
        while start<len(gas):
            # print(start)
            while(start<len(gas) and net[start]<0):
                start+=1
            if(start<len(gas) and visited[start]==0):
                visited[start]=1
            else:
                return -1 
                
            # print("start",start)
            sum=0
            flag=True
            for i in range (start,len(gas)):
                sum=sum+net[i]
                if(sum<0):
                    start=i+1
                    flag=False
                    break
            if flag:
                for i in range (0,start):
                    sum=sum+net[i]
                    if(sum<0):
                        start=i+1
                        flag=False
                        break
                
                if(sum>=0):
                    return start
        # print("sum",sum)
        if flag:
            start = start + 1
        return -1
