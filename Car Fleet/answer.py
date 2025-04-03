class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance=target
        l=len(speed)
        # time=[0]*l
        stack=[]
        for i in range(l):
            time=(distance-position[i])/speed[i]
            stack.append([time,position[i]])
        stack.sort(key=lambda x:x[1],reverse=True)
        # print(stack)
        max_time=stack[0][0]
        count=1
        # print(stack[1:])
        for ele in stack[1:]:
            i=ele[0]
            # print(i,max_time)
            if i<=max_time:
                continue 
            else:
                max_time=i
                count+=1
        return count 
