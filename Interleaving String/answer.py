class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        res=[[-1 for i in range( len(s1)+1)] for j in range( len(s2)+1)  ]
        def func(i,j,k):#s1 , s2 , s3 ptr
            # print(i,j,k," ",len(s3),len(s1)-1,len(s2)-1)
            # print(s1[i:],s2[j:],s3[k:])
            if res[j][i]!=-1:
                return res[j][i]
            if(k>=len(s3) and i==len(s1) and j==len(s2)): 
                return True
            elif(k>=len(s3)):
                return False

            a,b=False,False
            if(i<len(s1) and   s1[i]==s3[k]):
                a=func(i+1,j,k+1)

            if(j<len(s2) and s2[j]==s3[k]):
                b=func(i,j+1,k+1)

            # print(s1[i:],s2[j:],s3[k:],a or b)
            res[j][i]=a or b
            return a or b 
            

    
        return func(0,0,0)
        
