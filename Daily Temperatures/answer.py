class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t=temperatures
        stack=[]
        ans=[0]*len(t)
        for pos,i in enumerate(t):
            while(len(stack)>0 and  stack[-1][0]<i):
                stack_pos=stack[-1][1]
                ans[stack_pos]=pos-stack_pos
                stack.pop()
            stack.append([i,pos])
        return ans 
