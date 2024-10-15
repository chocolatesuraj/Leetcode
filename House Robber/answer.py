class Solution:
    def rob(self, nums: List[int]) -> int:
        cost=nums
        max1=cost[-1]
        n=len(cost)

        if(n==1):
            return max1
        max2=cost[-2]
        
        if(n==2):
            return max(max1,max2)
        max2=max(max1,max2)
        total=0
        for i in range(n-3,-1,-1):
            print(max2,max1)
            #res=cost[i]+ min(max1,max2)
            res=max(cost[i]+max1,max2)
            print(res)
            max1=max2
            max2=res
        return max(max1,max2)        
