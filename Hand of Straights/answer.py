class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        sort=sorted(set(hand))

        groups=len(hand)/groupSize
        print(groups)
        if(groups!=int(groups)):
            return False
        groups=int(groups)
        frequency_map = {}

        for item in hand:
            if item in frequency_map:
                frequency_map[item] += 1
            else:
                frequency_map[item] = 1
        lowptr=0
        lowp=sort[0]
        newlowp=0
        for i in range(groups):
            if(lowptr+groupSize<len(sort)):
                newlowp=sort[lowptr+groupSize]
                lowptr=lowptr+groupSize
                print('newloppp',newlowp)
            newlowptr=lowptr
            
            for i in range(groupSize-1,-1,-1):
                print('numner',lowp+i)
                if( (lowp+i) in frequency_map  and  frequency_map[lowp+i]>=1):
                    frequency_map[lowp+i]=frequency_map[lowp+i]-1
                    if(frequency_map[lowp+i]>=1):
                        newlowp=lowp+i
                        newlowptr=lowptr-(groupSize-i)
                        print('modifyy',newlowp,newlowptr)
                else:
                    return False
            lowp=newlowp
            lowptr=newlowptr
            
        return True 


    

        
