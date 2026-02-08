class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs=path.split("/")
        stack=[]

        for d in dirs:
            d.strip("/")
            if(d=="" or d=="."):
                continue
            elif(d==".."):
                if(stack):
                    stack.pop()
            else:
                stack.append(d)
            
        ans=""
        for d in stack:
            ans+="/"
            ans+=d
        if(ans==""):
            return "/"
        return ans
