class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bmap={"(":")",  "{":"}",  "[":"]"}
        for bracket in s:
            # print(stack,bracket)
            if stack==[] or not (stack[-1]in bmap and bmap[stack[-1]]==bracket):
                stack.append(bracket)
            elif stack[-1]in bmap and bmap[stack[-1]]==bracket:
                
                stack.pop(-1)
    
        if(stack==[]):
            return True 
        return False
