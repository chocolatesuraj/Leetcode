class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums=set(nums) 
        self.soln=[] 

        def perm(temp,nums):
            if(len(nums)==0):
                    self.soln.append(temp)
            for num in nums:
                
                newtemp=temp.copy()
                newtemp.append(num)
                newnums=nums.copy()
                newnums.remove(num)
                perm(newtemp,newnums)

        perm([],nums)
        return self.soln
