class Solution:
    def countSubstrings(self, s: str) -> int:
        def pal(s,l,r,leng):
            if(l-1>=0 and r+1<len(s) and s[l-1]==s[r+1]):
                self.count=self.count+1
                r=r+1
                l=l-1
                pal(s,l,r,leng)

        self.count=0
        for pos,i in enumerate(s):
            pal(s,pos,pos,1)
        for pos,i in enumerate(s[0:len(s)-1]):
            if(s[pos]==s[pos+1]):
                self.count=self.count+1
                pal(s,pos,pos+1,2)

        return self.count+len(s)
