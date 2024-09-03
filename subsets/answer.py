class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op=[[]]
        for num in nums:
            print("op= ",op)
            temp=[]
            for items in op :
                new =items.copy()
                new.append(num)
                temp.append(new)
            op.extend(temp)
        print (op)
        return op

