class Trie:

    def __init__(self):
        self.a=[None]*27
        self.end=False

        

    def insert(self, word: str) -> None:
        curr=self.a
        print("insertt")

        for char in word:

            num=ord(char)-ord('a')
            print(char)
            if(curr[num]==None):
                curr[num]=Trie()
            ender=curr[num]
            curr=curr[num].a
            

                
        ender.end=True
        

            
        

    def search(self, word: str) -> bool:
        curr=self
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxsearchh")
        for char in word:
            curr=curr.a
            print(char)
            num=ord(char)-ord('a')
            if(curr[num]!=None):
                ender=curr[num]
                curr=curr[num]
                
            else:
                return False
        if(ender.end==True):
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr=self
        for char in prefix:
            curr=curr.a
            num=ord(char)-ord('a')
            if(curr[num]!=None):
                curr=curr[num]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
