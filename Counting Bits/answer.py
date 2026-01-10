class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for num in range(0,n+1):
            i=num
            count=0
            # print("start",i)
            while(i):
                # print(i)
                if(i & 1 ==1):
                    count+=1
                i=i>>1
            ans[num]=count
        return ans
