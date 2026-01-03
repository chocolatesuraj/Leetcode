class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if(total%2==1):
            return False
        target=int(total/2)
        # print("target",target)
        self.target=target
        self.nums=nums
        self.mem=set()
        # print(self.mem)

        return self.check(0,0)
        # if(self.mem[target]==1):
        #     return True
        # return False

    def check(self,pos,cursum):
        # print(pos,cursum)
        # print(self.mem)
        if(cursum==self.target):
            return True
        if(cursum>self.target or pos==len(self.nums)):
            return False
        if((pos,cursum) not in self.mem):
            # print("test")
            ans= self.check(pos+1,cursum+self.nums[pos]) or self.check(pos+1,cursum)

            self.mem.add((pos,cursum))
            
            return ans 
        return False
                
