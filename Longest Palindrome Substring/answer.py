class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(s,l,r,leng):
            #print(s,l,r,leng)
            if(l-1>=0 and r+1<len(s) and s[l-1]==s[r+1]):
                leng=leng+2
                r=r+1
                l=l-1
                if(leng>self.maxlen):
                    self.maxstr=s[l:r+1]
                    self.maxlen=leng
                
                pal(s,l,r,leng)

        
        self.maxstr=s[0]
        self.maxlen=1
        for pos,i in enumerate(s):
            pal(s,pos,pos,1)
        for pos,i in enumerate(s[0:len(s)-1]):
            if(s[pos]==s[pos+1]):
                if(self.maxlen<2):
                    maxlen=2
                    self.maxstr=s[pos:pos+2]
                #print("cal2",pos,pos+1)
                pal(s,pos,pos+1,2)
        return self.maxstr

