class Solution:
    def numDecodings(self, s: str) -> int:
        if(int(s[0])==0):
            return 0
        arr=[]
        i=0
        while(i < (len(s)) ):
            print(s[i])
            
            if(int(s[i])>0 and (i+1<=len(s)-1)  and int(s[i+1])==0):
                num=int(s[i])*10
                if(num>26):
                    return 0
                arr.append(num) 
                i=i+1
            else:
                if(int(s[i])==0):
                    return 0
                
                arr.append(int(s[i]))
            i=i+1
        print(arr)
        
        if(len(arr)==1):
            return 1
        combs=1
        comb1=1
        comb2=1
        if(arr[0]*pow(10,len(str(arr[1])))+arr[1]<=26):
            combs=2
            comb1=1
            comb2=2
        if(len(arr)==2):
            return combs
        cont=False
        for i in range(2,len(arr)):
            if((arr[i]+arr[i-1]*pow(10,len(str(arr[i]))))<=26):
                combs=comb1+comb2
                comb1=comb2
                comb2=combs
                cont=True
            else:
                #comb2=combs
                comb1=comb2



        return combs
            


        
