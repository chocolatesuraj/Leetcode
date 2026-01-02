class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos=max(nums[0],0)
        neg=min(nums[0],0)
        ans=nums[0]
        if(len(nums)==1):
            return nums[0]
        for num in nums[1:]:
            # print("num",num)
            if(num>0):
                pos=max(pos*num,num)
                neg=neg*num
            elif(num<0):
                oldpos=pos
                pos=max(neg*num,0)
                neg=min(oldpos*num,num)
            if(max(pos,neg)>ans):
                ans=max(pos,neg)
            if(num==0):
                pos=0
                neg=0
            # print(pos,neg)
        return ans 
                
