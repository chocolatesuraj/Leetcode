class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashmap=dict()
        distlist=set()
        for ele in points:
            dist=sqrt(pow(ele[0],2)+pow(ele[1],2))
            distlist.add(dist)
            if(dist in hashmap):
                hashmap[dist].append(ele)
            else:
                hashmap[dist]=[ele]
        print(hashmap,distlist)
        soln=[]
        distlist=list(distlist)
        heapify(distlist)
        heap=distlist
        i=0
        while(i<k):
            a=heappop(heap)
            for x in hashmap[a]:
                i=i+1
                soln.append(x)
        return soln
