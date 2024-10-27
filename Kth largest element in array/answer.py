class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-x for x in nums]
        heapify(nums)
        for i in range(k):
            a=heappop(nums)
        return -a
