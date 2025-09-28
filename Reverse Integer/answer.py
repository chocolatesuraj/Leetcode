class Solution:
    def reverse(self, x: int) -> int:
        n= True if x<0 else False
        x=abs(x)
        ans=int(str(x)[::-1])
        ans=ans if n is False else -ans
        if((ans)< -(2**31) or ans>((2**31)-1)):
            return 0 
        return ans 
      
