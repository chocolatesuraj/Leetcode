class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.maxlen=1
        self.hashset=set()
        # lenght start finish 
        numlen=len(nums)
        def lon(leng,s,f,mini,maxi):
            if((leng,s,f,mini,maxi) in self.hashset):
                return 
            self.hashset.add((leng,s,f,mini,maxi))
            #print(s,f,leng)
            #print(self.hashset)
            if(leng>self.maxlen):
                self.maxlen=leng 
                #print("maxx",s,f,leng)
            if(f+1<numlen and nums[f+1]>maxi):
                lon(leng+1,s,f+1,mini,nums[f+1])
            if(f+1<numlen):
                lon(leng,s,f+1,mini,maxi)
            if(s-1>=0 and nums[s-1]<mini):
                lon(leng+1,s-1,f,nums[s-1],maxi)
            if(s-1>=0):
                lon(leng,s-1,f,mini,maxi)
        for i in range(1,len(nums)-1):
            lon(1,i,i,nums[i],nums[i])
        return self.maxlen


        
