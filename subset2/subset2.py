class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        print(nums)
        snums=sorted(nums)
        print(snums)
        my_dict = {}
        prev=None
        newnum=[]
        for i in snums:
            if i == prev:
                if i in my_dict:
                    my_dict[i] += 1
                else:
                    my_dict[i] = 1
            else:
                newnum.append(i)
                prev=i
        
        for i in newnum:
            if(i not in my_dict):    
                curres=res.copy()
                for ans in curres:
                    new=ans.copy()
                    new.append(i)
                    res.append(new)
                    print(ans)
            else:
                itr = my_dict[i]
                curres=res.copy()
                for ans in curres:
                    new=ans.copy()
                    new.append(i)
                    res.append(new)
                    for a in range(itr):
                        new=new.copy()
                        new.append(i)
                        res.append(new)

                    print(ans)
        print(res)
        return res

        


    
        
