class Solution:
   
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        starts=[]
        for num in nums:
            if(num-1 not in nums):
                starts.append(num)
        # print(starts)
        maxlen=0
        for s in starts:
            l=0
            i=0
            while(s+i in nums):
                l+=1
                i+=1
            if(l>maxlen):
                maxlen=l
        return maxlen

            

        
