class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap=Counter(t)
        tlen=len(t)
        ans=""
        alen=float("inf")
        f=0
        b=0
        bprev=-1
        while(bprev!=b):
            bprev=b
            while(tlen>0 and b<len(s)):
                # print(b)
                if(s[b] in tmap):
                    tmap[s[b]]-=1
                    if(tmap[s[b]]>=0):
                        tlen-=1
                b+=1
            while(True and f<len(s)):
                if(s[f] not in tmap):
                    f+=1
                elif(s[f] in tmap and tmap[s[f]]<0):
                    tmap[s[f]]+=1
                    f+=1
                else:
                    break
    
            if(tlen==0):
                # print(ans)
                if((b-f)<alen):
                    ans=s[f:b]
                    alen=b-f

            if(f+1<len(s)):
                tmap[s[f]]+=1
                f+=1
                # print(s[f])
                tlen+=1
            else:
                return ans
        return ans 

