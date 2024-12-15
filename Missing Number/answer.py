class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            ans=ans ^num
        for i in range(len(nums)+1):
            ans=ans ^ i
        return ans

        
