class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter=sum(matchsticks)
        side=perimeter//4
        if(side*4!=perimeter):
            return False
        sides=[0]*4
        matchsticks.sort(reverse=True)
        def backtrack(n):
            # print(n,sides)
            # if(sides[0:3]==[side,side,side]):
            #         return True
            if(n==len(matchsticks) ):
                return True

            stick=matchsticks[n]
            ans=False
            prev=None
            for s in range(4):
                # if s == prev:
                #     continue
                # prev=s
                if(stick+sides[s]<=side):
                    sides[s]=stick+sides[s]
                    ret=backtrack(n+1)
                    if(ret):
                        return True
                    sides[s]=sides[s]-stick

                    if sides[s] == 0: # if any one stick is bigger than the side 
                        break
            return False
        return backtrack(0)
