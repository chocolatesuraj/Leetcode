class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans=[]
        self.n=n
        stack=""
        self.sol(stack,n,n)
        return self.ans
    def sol(self,stack,op,close):
        if(op==0 and close==0):
            self.ans.append(stack)
        if(op<close):
            stack1=stack
            stack1=stack1+")"
            self.sol(stack1,op,close-1)
        if(op>0):
            stack2=stack
            stack2=stack+"("
            self.sol(stack2,op-1,close)
    
