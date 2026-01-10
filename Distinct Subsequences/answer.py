class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.s=s
        self.t=t
        self.ans=0
        self.memo=[[-1]*len(t) for i in range(len(s))]
        return self.f(0,0)
        # return self.ans
    def f(self,spos,tpos):
        # print(spos,tpos)
        
        if(spos>=len(self.s) or tpos>=len(self.t) ):
            return 0
        if(self.memo[spos][tpos]!=-1):
            return self.memo[spos][tpos]
        if self.s[spos]==self.t[tpos]:
            if (tpos==len(self.t)-1):
                # print("match",tpos)
                self.memo[spos][tpos]=1 + self.f(spos+1,tpos)
                return self.memo[spos][tpos]
            else:
                self.memo[spos][tpos]=self.f(spos+1,tpos) + self.f(spos+1,tpos+1)
                return self.memo[spos][tpos]

                

                 
        else:
            self.memo[spos][tpos]=self.f(spos+1,tpos)
            return self.memo[spos][tpos]

        
        
