class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        f=0
        b=0
        hm=set()
        hm.add(s[f])
        ans=1
        while b<len(s)-1:
            b=b+1
            #print(s[f:b])
            if(s[b] in hm):
                while(s[f]!=s[b]):
                    hm.remove(s[f])
                    f=f+1
                f=f+1
                
            else:
                hm.add(s[b])
                newlen=b-f+1
                #print(f,b,"else",newlen,hm)

                if(newlen>ans):
                    ans=newlen 

        return ans

            


        
