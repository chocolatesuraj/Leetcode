class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp={}
        def func(i,target):
            if((i,target) in self.dp):
                return self.dp[(i,target)]
            if(i==len(nums)-1):
                ans=0
                if(nums[i]==target):
                    ans+=1
                if(nums[i]==-target):
                    ans+=1
                return ans
            pos=target+nums[i]
            neg=target-nums[i]
            a=func(i+1,pos)
            b=func(i+1,neg)
            self.dp[(i,target)]=a+b
            return a+b 

        return func(0,target)      
