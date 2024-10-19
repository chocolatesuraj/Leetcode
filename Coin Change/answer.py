class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount==0):
            return 0
        coins.sort(reverse = True)
        sums={0}
        ans=0
        cont=True
        #tempsum=set()
        while(cont==True):
            tempsum=set()
            cont=False
            ans=ans+1
            for i in sums:
                for j in coins:
                    num=i+j
                    if(num<amount):
                        cont=True
                        tempsum.add(num)
                    elif(num==amount):
                        return ans
                    
            sums=tempsum
            #print(sums)
        return -1
