class Solution:
    def get_parent(self,curr):
        while(curr!=self.nodes[curr][0]):
            curr=self.nodes[curr][0]
        self.nodes[a][0]=curr
        return curr

    def union_find(self,a,b):
        a_parent=self.get_parent(a)
        b_parent=self.get_parent(b)
        if(a_parent==b_parent):
            return True
        return False

    def union_add(self,a,b):
        if(self.get_parent(a)!=self.get_parent(b)):
            ap,bp=self.nodes[self.get_parent(a)],self.nodes[self.get_parent(b)]
            if(ap[1]>bp[1]): # a has greater  rank make a parent 
                bp[0]=ap[0]
            elif(bp[1]>ap[1]): # b has greater  rank make a parent 
                ap[0]=bp[0]
            else:
                bp[0]=ap[0]
                ap[1]+=1

                


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.nodes={}
        for i in range(len(points)):
            self.nodes[i]=[i,0]
        # print(self.nodes)
        ans=0
        
        plist=[] # each element is of format [distance, point 1, point 2]
        for i,p1 in enumerate(points):
            for j,p2 in enumerate(points[i+1:]):
                if(p1!=p2):
                    dist=abs(p1[0]-p2[0])+  abs(p1[1]-p2[1])
                    plist.append([dist,i,j+i+1])

        
        # print(plist)
        plist.sort(key= lambda x: x[0])
        # print(plist)
        for ele in plist:
            p1=ele[1]
            p2=ele[2]
            if(self.union_find(p1,p2)==False):
                # print("False",p1,p2)
                self.union_add(p1,p2)
                # print(self.nodes)
                
                ans+=ele[0]
        return ans 


        

            

        
