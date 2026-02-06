class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        wr=0 # write pointer
        r=0 # read pointer
        prev=None
        while(r<len(nums)):
            if nums[r]==prev:
                r+=1
                continue
            prev=nums[r]
            if(wr==r):
                wr+=1
                r+=1
            else: #wr!=r
                nums[wr]=nums[r]
                wr+=1
                r+=1
        return wr




            
                
