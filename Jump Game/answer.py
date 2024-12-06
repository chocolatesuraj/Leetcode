class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end=len(nums)-1
        if(end==0):
            return True
        for i in range(1,len(nums)):
            pos=len(nums)-i-1
            print(pos,end-pos)
            if(nums[pos]>=(end-pos)):
                end=pos
        if(pos==end):
            return True
        return False

        
