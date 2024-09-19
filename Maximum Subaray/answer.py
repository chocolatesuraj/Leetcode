class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f=0
        l=len(nums)
        r=0
        onlyneg=True
        negnum=-99999
        maxsum=-9999999999
        cursum=0
        #checkk
        while(f<l):
            #print("cursum,maxsum=",cursum,maxsum,"l,r=",r,f)
           

            if(cursum+nums[f]<0):
                if(nums[f]>negnum):
                    negnum=nums[f]
                f=f+1
                cursum=0
                r=f
                
                #print(cursum)
            else:
                onlyneg=False
                cursum=cursum+nums[f]
                f=f+1
                #print(cursum)
            if(cursum>maxsum):
                maxsum=cursum
                
        #print(maxsum)
        if(onlyneg==True):
            return negnum
        return maxsum

        
