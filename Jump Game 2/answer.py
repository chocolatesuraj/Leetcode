class Solution:
    def jump(self, nums: List[int]) -> int:
        #print(nums)
        count=0
        l=len(nums)
        pos=l-1
        if(l==1):
            return 0
        for j in nums: # not meaning full just to iterate outer loop
            count=count+1
            for i,jump in enumerate(nums[0:pos]) :
                #print(i,pos,"jump+i=",jump+i)
                if(jump+i>=pos):
                    if(i==0):
                        return count
                    else:
                        #print(i)
                        pos=i
                        break
                        #return (self.canJump( nums[0:i+1]))
        return count
        
