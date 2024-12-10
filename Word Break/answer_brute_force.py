class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def check(l,r):
            #print(l,r)

            chunk=s[l:r+1]
            #print(chunk)

            if(r==len(s)-1 and (chunk in wordset)) :
                return True
            elif(r==len(s)-1):
                return False
            
            elif(chunk in wordset):
                return ( check(r+1,r+1) or check(l,r+1) )
                
            else:
                return check(l,r+1)

        wordset=set(wordDict)
        if (check(0,0)==True):
            return True
        return False
        
        

        
