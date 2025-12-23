class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=Counter(nums)
        # print(hashmap)
        res={}
        heap=[]
        for key,val in hashmap.items():
            if val not in res:
                res[val]=[key]
                heapq.heappush(heap,-val)
            else:
                res[val].append(key)

        # print("res",res)
        ans=[]
        while len(ans)<k:
            size=-heapq.heappop(heap)
            # print("size",size)
            ans=ans+res[size]

        return ans
        



