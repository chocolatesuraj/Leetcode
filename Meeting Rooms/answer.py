"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sort=sorted(intervals,key=lambda x: x.start)
        print(sort)
        maxx=0
        for tup in sort:
            print(tup)
            upper=tup.end
            down=tup.start
            
            if(down<maxx):
                return False
            if(upper>maxx):
                maxx=upper
        return True

