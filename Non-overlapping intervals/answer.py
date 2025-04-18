class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # print(intervals)
        ans=0
        prev=intervals[0]
        for i in intervals[1:]:
            if( i[0]<prev[1]):
                # print("collision",prev,i)
                ans+=1
                if(i[1]<prev[1]):
                    prev=i
            else:
                prev=i
        return ans
