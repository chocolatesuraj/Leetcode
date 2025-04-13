class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.sort()
        # # print(piles)
        l=1
        r=max(piles)
        ans=r
        while(l<=r):
            # print(l,r)
            m=int((l+r)/2)
            if self.possible(piles,h,m):
                if(m<ans):
                    ans=m
                r=m-1
                # print("llll ",l)
            else:
                # print("rrrr",r)
                l=m+1
        return ans

    
    def possible(self,piles,h,rate):
        time=0
        for i in piles:
            time+=math.ceil(i/rate)
        if(time<=h):
            return True 
        return False 
            

    

        
