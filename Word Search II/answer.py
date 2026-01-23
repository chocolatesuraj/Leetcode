class Node():
    def __init__(self):
        self.children=[None]*26
        self.isword=False
        self.word=""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = set()
        head=Node()

        def add_word(word):
            curr=head
            for w in word:
                pos=ord(w)-ord('a')
                if(curr.children[pos]==None):
                    curr.children[pos]=Node()
                curr=curr.children[pos]
            curr.isword=True
            curr.word=word




        def dfs(i, j, curr):
            a, b, c, d = False, False, False, False
            if(board[i][j]=="-1"):
                return 
            pos=ord(board[i][j])-ord("a")
            # print(i,j,pos)

            if curr.children[pos]!=None:
                child=curr.children[pos]
                # print("board match ")
                if child.isword==True:
                    # print("child word true",i,j,child)
                    ans.add(child.word)
                old = board[i][j]
                board[i][j] = "-1"

                if i - 1 >= 0:
                    a = dfs(i - 1, j, child)
                if i + 1 < len(board):
                    b = dfs(i + 1, j, child)
                if j - 1 >= 0:
                    c = dfs(i, j - 1, child)
                if j + 1 < len(board[0]):
                    d = dfs(i, j + 1, child)
                board[i][j] = old
                if a and b and c and d:
                    # curr.children=[None]*26
                    curr=None
                #     return True
                # return False

        def find():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    # print(dfs,i,j)
                    if(len(ans)==len(words)):
                        return ans
                    dfs(i, j, head)
                        

        for word in words:
            add_word(word)
        find()
        return list(ans)
