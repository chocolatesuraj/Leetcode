class Solution:
    def __init__(self):
        self.grid=None


    def longestCommonSubsequence(self, text1: str, text2: str,ptr1=0,ptr2=0) -> int:
        self.grid=[[-1 for i in range (len(text1))] for j in range (len(text2))]
        print(self.grid)
        self.text1=text1
        self.text2=text2
        self.setup=True
        return self.lcs(ptr1,ptr2)

    def lcs(self,ptr1=0,ptr2=0) -> int:
        # print(self.text1[ptr1:],self.text2[ptr2:])
        
        if(ptr1>=len(self.text1) or ptr2>=len(self.text2)):
            # print(self.text1[ptr1:],self.text2[ptr2:],0)
            return 0
        # print(ptr1,ptr2)
        if(self.grid[ptr2][ptr1]!=-1):
            return self.grid[ptr2][ptr1]
        if(self.text1[ptr1:]=="" or self.text2[ptr2:]==""):
            self.grid[ptr2][ptr1]=0
            return 0
        elif(self.text1[ptr1]==self.text2[ptr2]):
            ans= 1+ self.lcs(ptr1+1,ptr2+1)
            self.grid[ptr2][ptr1]=ans
            # print(self.text1[ptr1:],self.text2[ptr2:],ans)
            # print(self.grid)
            return ans
        else:
            ans= max(self.lcs(ptr1+1,ptr2),self.lcs(ptr1,ptr2+1))
            self.grid[ptr2][ptr1]=ans
            # print(self.text1[ptr1:],self.text2[ptr2:],ans)

            # print(self.grid)

            return ans
