class Solution(object):
    def __init__(self):
        self.hashmap={}
        self.ans=0
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        if(n==0):
            ans=ans+1
            return 1
        if(n==1):
            ans=ans+1
            return 1
        if(n==2):
            ans=ans+2
            return 2
        if n in self.hashmap:
                return self.hashmap[n]
        
        for i in range(1,n+1):
            print(i)
            soln=self.numTrees(i-1)*self.numTrees(n-i)
            ans=ans+soln
        self.hashmap[i]=ans
        return ans
            
    

            



        
