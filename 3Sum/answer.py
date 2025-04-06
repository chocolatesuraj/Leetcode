class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        prev=None
        ans=[]
        a=0
        while a<len(nums):
            # print("new",a,prev)
            while(nums[a]==prev):
                if(a+1<len(nums)):
                    a+=1
                else:
                    return ans
            prev=nums[a]
            l=a+1
            r=len(nums)-1
            while(l<r):
                # print(a,l,r)
                summ=nums[a]+nums[l]+nums[r]
                if(summ==0):
                    ans.append([nums[a],nums[l],nums[r]])
                    prevr=r
                    while(r>0 and nums[prevr]==nums[r]):
                        r=r-1
                elif(summ>0):
                    r=r-1
                else:
                    l=l+1
            a+=1
        return ans 
