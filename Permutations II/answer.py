class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # ans=[]
        # temp=[]
        nums.sort()
        def permutations(numbs):
            # print(numbs)
            ans=[]
            prev=None
            for i,numb in enumerate(numbs):
                if(numb==prev):
                    continue
                # print(numb,numbs)
                
                prev=numb
                l=len(numbs)
                if(len(numbs)==1):
                    return [numbs]
                perms=permutations(numbs[0:i]+numbs[i+1:l])
                # print(perms)
                ans+=[[numb]+perm for perm in perms ]
            # print(ans)
            return ans

        return permutations(nums)
        

        # def perms(ele_set):
        #     for i i
