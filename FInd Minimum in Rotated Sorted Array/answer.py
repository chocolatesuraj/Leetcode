class Solution:
    

    def findMin(self, nums: List[int]) -> int:
        r=len(nums)-1
        l=0
        mid=int((l+r)/2)
        
        while(l<r):
            mid=int((l+r)/2)
            print(l,mid,r)
            if(mid>len(nums)-2):
                break
            if(nums[mid+1]<nums[mid]):
                break
            if(nums[mid]>nums[r]):
                l=mid
            else:
                r=mid
        print(mid)
        a=nums[0]
        if(mid+1<len(nums)):
            b=nums[mid+1]
        else:
            b=nums[mid]
        return min(a,b)
        


        
