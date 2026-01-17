class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts=Counter(nums)
        maxi=0
        ans=None
        for num,count in counts.items():
            if(count>maxi):
                ans=num
                maxi=count
        return ans
