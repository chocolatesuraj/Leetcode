class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        c=[]
        ans=[]
        def comb(i):
            if(i>n):
                return 
            c.append(i)
            if(len(c)==k):
                ans.append(c[:])
            else:
                comb(i+1)
            c.pop()
            comb(i+1)
        comb(1)
        return ans 
                

            
