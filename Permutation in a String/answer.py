class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        onelen=len(s1)
        hashmap={}
        for i in "abcdefghijklmnopqrstuvwxyz":
            hashmap[i]=0
        for i in s1:
                hashmap[i]= hashmap[i]+1
        checkmap={}
        for i in "abcdefghijklmnopqrstuvwxyz":
            checkmap[i]=0
        i=0
        while (i<len(s1)):
            checkmap[s2[i]]=checkmap[s2[i]]+1
            i=i+1
        j=0
        i=i-1
        count=onelen
        while (i<len(s2)):
            print(s2[j],s2[i])
            if(checkmap==hashmap):
                print("trueee")
                return True 
            if(i+1>=len(s2)):
                return False
            i=i+1
            checkmap[s2[i]]= checkmap[s2[i]]+1
            checkmap[s2[j]]= checkmap[s2[j]]-1
            j=j+1
        return False


        
