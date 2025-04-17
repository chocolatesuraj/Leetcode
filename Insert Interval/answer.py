class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        if(intervals==[]):
            ans.append(newInterval)
            return ans
        intervalscopy=intervals
        for i,interval in enumerate(intervalscopy):
            start,end=interval[0],interval[1]
            newstart,newend=newInterval[0],newInterval[1]
            # print(ans,interval,newInterval)
            if(newstart>end):
                # print("after current interval case")
                ans.append(interval)
                continue 
            elif(newend<start):
                # print("before current interval case")
                if(len(ans)==0 or ans[-1]!=newInterval): #already insrted by merge case 2 
                    ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans
            elif(newend>=end and newstart<=end):
                # print("merge case- new interval exceed current interval")
                newInterval=[min(start,newstart),max(newend,end)]
            elif(newend<=end and newend>=start ):
                # print("merge case 2 current interval is the end of merge")
                newInterval=[min(start,newstart),max(newend,end)]
                ans.append(newInterval)
                ans.extend(intervals[i+1:])
                return ans
        ans.append(newInterval)
        return ans



            
