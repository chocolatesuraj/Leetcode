class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals= sorted(intervals, key=lambda x: x[0])
        prev=intervals[0]
        mini=intervals[0][0]
        maxi=intervals[0][1]
        ans=[]
        for ele in intervals[1:]:
            print(mini,maxi)
            print(ele[0])
            if(ele[0]>maxi):
                end=True
                ans.append([mini,maxi])
                prev=ele
                mini=ele[0]
                maxi=ele[1]
                print(ele,"maxx",maxi)
            else:
                end=False
                mini=min(ele[0],mini)
                maxi=max(ele[1],maxi)
        
        ans.append([mini,maxi])
        
        return ans
        
