class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #visited array is used to store courses that are completed and have no more requiements
        pre=dict()
        for ele in prerequisites:
            i,j = ele 
            if i not in pre:
                pre[i]=[j]
            else:
                pre[i].append(j)
        soln=[]
        visited=[0]*numCourses
        loop=[0]*numCourses
        print(visited)
        flag=True
        def bfs(i)->bool:
            if(visited[i]==1):
                return True
            print("current",i)
            #print(visited)
            if(loop[i]==1):
                print("falsee")
                return False
            
            loop[i]=1
            if((i not in pre) or pre[i]==[] ):
                #print("append",i)
                #loop[:] = [0] * numCourses
                soln.append(i)
                visited[i]=1
            else:
                for ele in pre[i]:
                    if(loop[ele]==1 and visited[ele]==0):
                        #print("flaseeee",ele,i)
                        return False
                    #print(ele)
                    #visited[ele]=1
                    ans=bfs(ele)
                    if(ans==False):
                        print("falsee")
                        return False
                    visited[ele]=1
                    
                #print("append--",i)
                visited[i]=1
                soln.append(i)
               
        for i in range(0,numCourses):
            if(visited[i]==0):
                a=bfs(i)
                loop=[0]*numCourses
                if(a==False):
                    return []
        return soln



                


                


        
