class Solution:

    def encode(self, strs: List[str]) -> str:
        # format- num , delimiter word, 
        ans=""
        for word in strs:
            l=len(word)
            ans+=str(l)
            ans+="#"
            ans+=word
        print(ans)
        return ans


    def decode(self, s: str) -> List[str]:
        num=""
        i=0
        words=[]
        while(i<len(s)):
            num=""
            while(s[i]!="#"):
                print(num," ",s[i])
                num+=s[i]
                i+=1
            print("num before int",num,len(num))
            num=int(num)
            print(num)
            i+=1
            word=s[i:i+num]
            print(word)
            i=i+num
            print("new i",i)
            words.append(word)
        return words
