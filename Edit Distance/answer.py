class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem=[[-1 for i in range(len(word2)+1)]for i in range(len(word1)+1)]

        def func(i,j):
            if(mem[i][j]!=-1):
                return mem[i][j]
            if(j==len(word2)):
                ans =max(len(word2)- j , len(word1)-i)
                # print(word1[i:],word2[j:],ans,"  end word2")
                mem[i][j]=ans
                return ans 
            if(i==len(word1)):
                ans= max(len(word2)- j , len(word1)-i)
                # print(word1[i:],word2[j:],ans,"   end word 1")
                mem[i][j]=ans
                return ans 
            if(word1[i]==word2[j]):
                ans= (func(i+1,j+1))
                # print(word1[i:],word2[j:],ans ,"equal")
                mem[i][j]=ans
                return ans 
            else:
                a=  1+ func(i+1,j) #delete letter
                b= 1+ func(i+1,j+1) #replace character 
                c= 1+ func(i,j+1) # insert character
                ans= min(a,b,c)
                # print(word1[i:],word2[j:],ans)
                mem[i][j]=ans
                return ans 
        
        
        return func(0,0)
            


        
