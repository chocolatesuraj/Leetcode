class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        max1=cost[-1]
        max2=cost[-2]
        n=len(cost)
        if(n==1):
            return max1
        if(n==2):
            return min(max1,max2)
        total=0
        for i in range(n-3,-1,-1):
            print(max2,max1)
            res=cost[i]+ min(max1,max2)
            print(res)
            max1=max2
            max2=res
        return min(max1,max2)


