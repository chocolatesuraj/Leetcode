class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f=0
        b=len(heights)-1
        maxvol=0
        while(f!=b):
            vol=abs(min(heights[f],heights[b])*(f-b))
            # print(f,b,vol)
            if(vol>maxvol):
                maxvol=vol
            if(heights[f]>heights[b]):
                b=b-1
            else:
                f=f+1
        return maxvol

        
