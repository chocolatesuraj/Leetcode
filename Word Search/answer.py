class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(i,j,ele,wpos,visited):
            #print(visited)
            #print(ele)
            a=False
            b=False
            c=False
            d=False
            if i + 1 < h and board[i + 1][j] == ele and (i+1,j) not in visited:
                new1=visited.copy()
                new1.add((i+1,j))
                if(wpos==len(word)-1):
                    return True
                a= find(i + 1, j,word[wpos+1], wpos + 1,new1)
            if i - 1 >= 0 and board[i - 1][j] == ele and (i-1,j) not in visited:
                new2=visited.copy()
                new2.add((i-1,j))
                if(wpos==len(word)-1):
                    return True
                b= find(i - 1, j, word[wpos+1], wpos + 1,new2)
            if j + 1 < w and board[i][j + 1] == ele and (i,j+1) not in visited:
                new3=visited.copy()
                new3.add((i,j+1))
                if(wpos==len(word)-1):
                    return True
                c= find(i, j + 1, word[wpos+1], wpos + 1,new3)
            if j - 1 >= 0 and board[i][j - 1] == ele and (i,j-1) not in visited:
                new4=visited.copy()
                new4.add((i,j-1))
                if(wpos==len(word)-1):
                    return True
                d=find(i, j - 1, word[wpos+1], wpos + 1,new4)
            #print(ele,a,b,c,d,wpos,len(word)-1)
            if(a==True or b==True or c==True or d==True):
                return True

            return False
        h=len(board)
        w=len(board[0])
        wpos=0
        ans=False
        for i in range(h):
            for j in range (w):
                if(board[i][j]==word[wpos]):
                    #print("new")
                    if(len(word)==1):
                        return True
                    visited=set()
                    visited.add((i,j))
                    ans=find(i,j,word[wpos+1],wpos+1,visited)
                    if(ans==True):
                        return ans
        return ans
        

        



