class Solution:
    def hammingWeight(self, n: int) -> int:
        num=1
        ans=0
        for i in range(32):
            print(num)
            if(num & n == num):
                ans=ans+1
            num=num*2
        return ans

        
