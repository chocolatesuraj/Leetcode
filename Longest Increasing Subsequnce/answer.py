class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums=nums
        m=0
        self.memo=[-1]* len(nums)#0- retrun value
        # print(self.memo)
        for i in range(0,len(nums)):
            m=max(m,self.lis(i,-float("inf")))
        # print(self.memo)
        return m

    def lis(self,pos,prev):
        if(self.memo[pos]!=-1 and self.nums[pos]>prev ):
            return self.memo[pos]
        l=0
        if(pos<len(self.nums)):
            # print(self.nums[pos],prev)
            if(self.nums[pos]>prev):
                l+=1
                maxi=0
                for i in range(pos+1,len(self.nums)):
                    a=self.lis(i,self.nums[pos])
                    maxi=max(a,maxi)
                self.memo[pos]=l+maxi
                return l+maxi
            else:
                return 0

