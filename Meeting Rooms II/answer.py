import bisect
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda obj:obj.start)
        # print(intervals)
        ends=[]
        for interval in intervals:
            if ends==[]:
                heapq.heappush(ends,interval.end)
            elif(interval.start>=ends[0]):
                heapq.heappop(ends)
                heapq.heappush(ends,interval.end)
            elif(interval.start<ends[0]):
                heapq.heappush(ends,interval.end)
        return len(ends)
        
