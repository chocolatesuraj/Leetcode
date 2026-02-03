class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        store=deque()#each element - [num,index]
        ans=[]
        appendptr=0
        for i,num in enumerate(nums):
            temp=[]
            # and i-store[-1][1]<k
            while( store  and num>store[-1][0]  ) :
                # print("loop",store)
                n,l=store.pop()
            while ( store and i-store[0][1]>=k ):
                store.popleft()
                # temp.append([num,l])
            
            
            store.append([num, i])
            ans.append(store[0][0])
            # print(store)

        
        return ans[k-1::]
