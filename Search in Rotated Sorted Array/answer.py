class Solution:
    def binsearch(self, nums: List[int], target: int):
        print("binsearch",nums,target)
        r=len(nums)-1
        l=0
        
        while(l<=r):
            mid=int((l+r)/2)
            print(l,mid,r)
            if(target==nums[mid]):
                print("return mid",mid)
                return mid
            if(target> nums[mid]):
                l=mid+1
            else:
                r=mid-1
        print("return -1")
        return -1



    def search(self, nums: List[int], target: int) -> int:
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
        a=self.binsearch(nums[mid+1:],target)
        b=self.binsearch(nums[:mid+1],target)
        if(a==-1 and b==-1):
            return -1
        if(a==-1):
            return b
        if(b==-1):
            return a+mid+1
       
        
