class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if(len(nums)==1):
            return nums[0]
        i=0
        if(nums[i]!=nums[i+1]):
            return nums[i]
        while(i+1<len(nums)):
            if(nums[i]==nums[i+1]):
                i=i+2
            else:
                return nums[i]
        return  nums[-1]


        
