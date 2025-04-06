class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if(t!="+" and t!="*" and t!="-" and t!="/"):
                stack.append(t)
            else:
                a=int(stack.pop())
                b=int(stack.pop())
                if(t=="+"):
                    ans=a+b
                elif(t=="-"):
                    ans=b-a
                elif(t=="*"):
                    ans=a*b
                elif(t=="/"):
                    ans=b/a
                stack.append(ans)
            # print(stack)
        return int(stack[0])

        
