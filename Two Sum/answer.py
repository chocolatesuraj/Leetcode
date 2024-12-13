class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        posmap={}
        for pos,num in enumerate(nums):
            if(num not in posmap):
                posmap[num]=[pos]
            else:
                print(posmap)
                posmap[num].append(pos)

        print(posmap)
        nums=sorted(nums)
        print(nums)
        r=len(nums)-1
        l=0
        while(l<r):
            s=nums[l]+nums[r]
            if(s==target):
                if(nums[l]==nums[r]):
                    return[posmap[nums[l]][0],posmap[nums[r]][1]]
                return[posmap[nums[l]][0],posmap[nums[r]][0]]
            elif(s>target):
                r=r-1
            else:
                l=l+1
            
        
