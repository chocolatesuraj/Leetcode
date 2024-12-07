class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pos=0
        self.soln=[]
        self.combsum(candidates,[],target,0,0)
        return self.soln

    def combsum(self,arr,temp,target,pos,oldsum):
        if(oldsum>target):
            return 
        elif(oldsum==target):
            #ntemp.append(arr[pos])
            self.soln.append(temp)
            return 
        
        elif(pos==len(arr)):
            return 
        newsum=arr[pos]+oldsum
        ntemp=temp.copy()

        ntemp.append(arr[pos])
        print(temp,pos,newsum,"onee")
        self.combsum(arr,ntemp,target,pos,newsum)

        ctemp=temp.copy()
        print(temp,pos+1,oldsum,"twooo")
        self.combsum(arr,ctemp,target,pos+1,oldsum)
        
        
        
        
            
