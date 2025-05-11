class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        maxheap=[]
        for i in range(0,k):
            heapq.heappush(maxheap,(-nums[i],i))

        ans.append(-maxheap[0][0])

        for i in range(k,len(nums)):
            while(len(maxheap)>0 and maxheap[0][1]<i-k+1):
                heapq.heappop(maxheap)
            heapq.heappush(maxheap,(-nums[i],i))
            ans.append(-maxheap[0][0])

        return ans 
