class Solution:
    def reverseBits(self, n: int) -> int:
        mask=1
        ans=0
        for i in range(1,33):
            print(mask,n)
            if(mask &  n == mask):
                ans=ans+pow(2,(32-i))
            mask=mask*2
        return ans




        
