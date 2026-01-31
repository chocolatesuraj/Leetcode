class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        f,b=0,len(nums)-1
        m=f
        if(target<nums[0]):
            return 0
        if(target>nums[-1]):
            return len(nums)
        while(f<=b):
            m=int((f+b)/2)
            # print(f,b,"  ",m)
            if(nums[m]==target):
                return m
            elif(nums[m]<target):
                f=m+1
            else:
                b=m-1
        if(nums[m]<target):
            return m+1
        return m
