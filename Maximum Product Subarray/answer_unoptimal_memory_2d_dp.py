class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp=[[-1 for i in range(len(nums))] for i in range( len(nums))]
        def func(i,j):
            if(dp[i][j]!=-1):
                return  dp[i][j]
            if(i>j):
                return 0 
            if(i==j):
                ans= nums[i]
                dp[i][j]=ans
                return ans
            else:
                ans= nums[i]*func(i+1,j)
                dp[i][j]=ans
                return ans
        maxi=-99999999999
        for i in range(len(nums)):
            for j in range(len(nums)):
                prod=func(i,j)
                if(prod>maxi):
                    maxi=prod
        return maxi
