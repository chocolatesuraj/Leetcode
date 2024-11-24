class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap=dict()
        if(n==1 and edges==[]):
            return True
        for ele in edges:
            i,j=ele
            if(i==j):
                return False
            if(i not in hashmap):
                hashmap[i]=[j]
            else:
                hashmap[i].append(j)
            if(j not in hashmap):
                hashmap[j]=[i]
            else:
                hashmap[j].append(i)
        print(hashmap)
        self.visited=set()
        self.tempvisited=set()
        nextt=[0]
        
        def bfs(num)->list:
            temp=[]
            for  ele in hashmap[num]:
                if(num in hashmap[ele]):
                    hashmap[ele].remove(num)
                if((ele in self.visited) and(ele !=num)):
                    print("falseeee")
                    return None
                print("ele",ele)
                self.visited.add(ele)
                temp.append(ele)
            return temp
            
            return []

        
        for num in nextt: 
            self.visited.add(num) 
            print(num)    
            temp=bfs(num)
            print("Tempp",temp)
            if(temp!=None):  
                #self.visited=self.visited | self.tempvisited
                nextt.extend(temp)
            elif(temp==None):
                return False
        l=len(self.visited)
        print("lennn",l,n)
        print(self.visited)
        if(l<n):
            return False
        return True

            
            
            
            
