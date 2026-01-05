class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net=[gas[i]-cost[i] for i in range(len(gas))]
        print(net)

        if(sum(net)<0):
            return -1
        total=0
        start=None
        for i,val in enumerate(net):
            # print(val,total)
            if(start==None):
                start=i
            total+=val
            if(total<0):
                total=0
                start=None
        return start
