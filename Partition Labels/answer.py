class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap={}
        for c in s:
            if(c in hashmap):
                hashmap[c]=hashmap[c]+1
            else:
                hashmap[c]=1
        print (hashmap) 
        ans=[]
        listptr=0
        l=0
        i=0
        while(i<len(s)):
            c=s[i]
            #l=l+1
            #hashmap[c]=hashmap[c]-1
            print(c,listptr,hashmap)
            
            if(hashmap[c]==0  and (listptr==i) ):
                ans.append(l)
                l=0
                i=i+1
            elif(hashmap[c]==0 and  listptr<i and hashmap[s[listptr]]==0):
                listptr=listptr+1
            elif(hashmap[c]!=0):
                hashmap[c]=hashmap[c]-1
                l=l+1
                if(hashmap[c]!=0):
                    i=i+1
            else:
                i=i+1
            
        return ans

        
            

            
        return []        
