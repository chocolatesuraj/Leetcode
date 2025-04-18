class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cm={} #collision map to track collisions 
        self.ans=0
        for i,in1 in enumerate(intervals):
            for j,in2 in enumerate(intervals):
                if(self.iscollide(in1,in2) and i!=j):
                    if(i in cm):
                        cm[i].add(j)
                    else:
                        cm[i]=set()
                        cm[i].add(j)
                    if(j in cm):
                        cm[j].add(i)
                    else:
                        cm[j]=set()
                        cm[j].add(i)
        print(cm)
        self.cm=cm
        print(self.cm)
        while self.cm:
            # Find the interval with the most collisions
            max_collisions = 0
            max_key = None
            
            for key, val_set in self.cm.items():
                if len(val_set) > max_collisions:
                    max_collisions = len(val_set)
                    max_key = key
            
            # Delete the interval with most collisions
            self.delete(max_key)
        
        return self.ans

        return self.ans
        
    
    def delete(self,key):
        print("key",key)
        if(key not in self.cm):
            return 
        self.ans+=1
        for i in self.cm[key]:
            self.cm[i].remove(key)
            if(len(self.cm[i])==0):
                self.cm.pop(i)
        self.cm.pop(key)
                

    def iscollide(self,i,j):
        print(i,j)
        if(i[1]<=j[0] or i[0]>=j[1]):
            print(False)
            return False
        print(True)
        return True 
        
