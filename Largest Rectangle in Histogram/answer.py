class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  
        ans=0
        stack=[] # list of lists with index , height 
        for i,h in enumerate(heights):
            if(len(stack)==0 or stack[-1][1]<=h):
                stack.append([i,h])
            else:
                while(len(stack)>0 and   stack[-1][1]>h):
                    top=stack.pop()
                    area=top[1]*(i-top[0])
                    if(area>ans):
                        ans=area
                stack.append([top[0],h])
        # print(stack)
        while(len(stack)>0):
            top=stack.pop()
            area=top[1]*(len(heights)-top[0])
            if(area>ans):
                ans=area


        return ans

        
