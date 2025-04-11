class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t=temperatures
        # print(ans)
        future=[0]*71
        stack=[]
        future[t[-1]-30]=len(t)-1
        stack.append(future)
        for i in range(len(t)-2,-1,-1):
            # print(i)
            newstack=stack[-1].copy()
            # print(t[i]-30)
            newstack[t[i]-30]= i
            stack.append(newstack)
        # print(len(stack))
        ans=[]
        for curpos,ele in enumerate(t):
            top=stack.pop()
            day=999999
            for i,j in enumerate(top):
                # print(i+30,ele,j)
                if(j!=0 and j-curpos<day  and i+30>ele ):
                    day=j-curpos
                    # print("settt")
            if(day==999999):
                day=0
           

            ans.append(day)
        return ans
               
            
            

            

        
