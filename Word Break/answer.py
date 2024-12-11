class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.ans=False
        self.dp=[0]*len(s)
        print(self.dp)
        
        def check(l,r):
            c=False
            print(l)
            if(self.dp[l]==1):
                return False
            for word in wordDict:
                if(self.ans==False):
                    wl=len(word)
                    #print(l,wl,wl+l,r)
                    #print(s[l:l+wl])
                    if(wl<=r and s[l:l+wl]==word):
                        print(s[0:l+wl], wl+l,r)
                        c=True
                        if(wl+l==r):
                            self.ans=True
                            return True
                            
                        c=check(l+wl,r)
            if(c==False):
                self.dp[l]=1
                return False
            

        check(0,len(s))
        return self.ans

        #acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb
        #acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb
        
        

        
