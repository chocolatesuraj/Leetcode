class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete=True
        #abc  cbca 
        def pal(f,b):
            nonlocal delete
            while f<b:
                if(s[f]==s[b]):
                    f+=1
                    b-=1
                else:
                    x,y=False,False
                    if(delete==False):
                        return False
                    delete=False
                    if(s[f+1]==s[b]):
                        x=pal(f+1,b)
                    if(s[b-1]==s[f]):
                        y=pal(f,b-1)
                    
                    return x or y
            return True
        return pal(0,len(s)-1)
